import os
import json
from collections import defaultdict
from typing import Dict, List, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class N8nWorkflowAnalyzer:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.node_types = defaultdict(int)
        self.node_connections = defaultdict(list)
        self.node_parameters = defaultdict(list)
        self.workflow_patterns = []
        self.error_files = []

    def find_workflow_files(self) -> List[str]:
        """Find all .txt files containing n8n workflows"""
        workflow_files = []
        for root, _, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith('.txt'):
                    workflow_files.append(os.path.join(root, file))
        return workflow_files

    def parse_workflow(self, file_path: str) -> Dict[str, Any]:
        """Parse a single workflow file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Try to find the first valid JSON object
                try:
                    return json.loads(content)
                except json.JSONDecodeError:
                    # If the file contains multiple JSON objects, try to parse the first one
                    start_idx = content.find('{')
                    end_idx = content.rfind('}')
                    if start_idx != -1 and end_idx != -1:
                        try:
                            return json.loads(content[start_idx:end_idx+1])
                        except json.JSONDecodeError:
                            self.error_files.append((file_path, "Invalid JSON format"))
                            return {}
                    else:
                        self.error_files.append((file_path, "No JSON object found"))
                        return {}
        except Exception as e:
            self.error_files.append((file_path, str(e)))
            logger.error(f"Error parsing {file_path}: {str(e)}")
            return {}

    def analyze_workflow(self, workflow: Dict[str, Any], file_name: str):
        """Analyze a single workflow's structure"""
        if not workflow:
            return

        # Analyze nodes
        for node in workflow.get('nodes', []):
            node_type = node.get('type', '')
            node_name = node.get('name', '')
            
            # Track node types
            self.node_types[node_type] += 1
            
            # Track node parameters
            if 'parameters' in node:
                self.node_parameters[node_type].append(node['parameters'])

        # Analyze connections
        connections = workflow.get('connections', {})
        for source, targets in connections.items():
            if not isinstance(targets, dict):
                continue
            for target_list in targets.values():
                if not isinstance(target_list, list):
                    continue
                for target in target_list:
                    if isinstance(target, dict) and 'node' in target:
                        self.node_connections[source].append(target['node'])

        # Track workflow pattern
        pattern = self._extract_workflow_pattern(workflow)
        if pattern:
            self.workflow_patterns.append({
                'file': file_name,
                'pattern': pattern
            })

    def _extract_workflow_pattern(self, workflow: Dict[str, Any]) -> List[str]:
        """Extract the sequence of node types in the workflow"""
        try:
            nodes = {node['id']: node['type'] for node in workflow.get('nodes', [])}
            pattern = []
            
            # Find start nodes
            start_nodes = [node for node in workflow.get('nodes', []) 
                          if node.get('type') == 'n8n-nodes-base.start']
            
            for start in start_nodes:
                current = start['id']
                while current in workflow.get('connections', {}):
                    pattern.append(nodes.get(current, ''))
                    next_nodes = workflow['connections'][current].get('main', [[]])[0]
                    if not next_nodes:
                        break
                    current = next_nodes[0]['node']
            
            return pattern
        except Exception as e:
            logger.error(f"Error extracting workflow pattern: {str(e)}")
            return []

    def generate_syntax_manual(self) -> str:
        """Generate a comprehensive syntax manual"""
        manual = []
        
        # Section A: Node Types & Frequency
        manual.append("Section A: Node Types & Frequency")
        manual.append("-" * 40)
        for node_type, count in sorted(self.node_types.items(), key=lambda x: x[1], reverse=True):
            manual.append(f"- {node_type}: {count} uses")
        manual.append("\n")

        # Section B: Common Node Connections
        manual.append("Section B: Common Node Connections")
        manual.append("-" * 40)
        for source, targets in self.node_connections.items():
            manual.append(f"- {source} → {', '.join(targets)}")
        manual.append("\n")

        # Section C: Workflow Patterns
        manual.append("Section C: Common Workflow Patterns")
        manual.append("-" * 40)
        pattern_counts = defaultdict(int)
        for pattern in self.workflow_patterns:
            pattern_str = " → ".join(pattern['pattern'])
            pattern_counts[pattern_str] += 1
        
        for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True):
            manual.append(f"- {pattern}: {count} occurrences")
        manual.append("\n")

        # Section D: Node Parameters
        manual.append("Section D: Node Parameter Patterns")
        manual.append("-" * 40)
        for node_type, params_list in self.node_parameters.items():
            if params_list:
                manual.append(f"\n{node_type}:")
                # Analyze common parameters
                param_keys = set()
                for params in params_list:
                    param_keys.update(params.keys())
                manual.append(f"  Common parameters: {', '.join(sorted(param_keys))}")

        # Section E: Error Report
        if self.error_files:
            manual.append("\nSection E: Files with Errors")
            manual.append("-" * 40)
            for file_path, error in self.error_files:
                manual.append(f"- {os.path.basename(file_path)}: {error}")

        return "\n".join(manual)

    def analyze_all_workflows(self):
        """Analyze all workflows in the directory"""
        workflow_files = self.find_workflow_files()
        logger.info(f"Found {len(workflow_files)} workflow files")

        for file_path in workflow_files:
            logger.info(f"Analyzing {file_path}")
            workflow = self.parse_workflow(file_path)
            self.analyze_workflow(workflow, os.path.basename(file_path))

        return self.generate_syntax_manual()

def main():
    # Update this to your actual workflow directory
    root_dir = "F:/automation/awesome-n8n-templates"
    
    analyzer = N8nWorkflowAnalyzer(root_dir)
    syntax_manual = analyzer.analyze_all_workflows()
    
    # Save the syntax manual
    with open("n8n_syntax_manual.txt", "w", encoding="utf-8") as f:
        f.write(syntax_manual)
    
    logger.info("Syntax manual generated successfully!")

if __name__ == "__main__":
    main()