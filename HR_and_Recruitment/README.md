# AI-Driven HR Automation & Chatbot Templates for n8n

A curated collection of advanced n8n workflow templates designed to supercharge HR and recruitment operations with AI, automation, and seamless integrations. These templates streamline job posting, candidate evaluation, helpdesk support, and company policy management using state-of-the-art AI models and best practices in workflow automation.

---

## Included Templates

### 1. HR Job Posting and Evaluation with AI
- **Purpose:** Automates the end-to-end process of job posting, candidate application collection, and multi-stage evaluation.
- **Features:**
  - Custom job application forms (with CV upload)
  - Airtable integration for applicant tracking
  - AI-powered CV and job description matching and scoring
  - Multi-stage evaluation (application, phone, onsite, etc.)
  - Automated notifications and data routing
- **Use Case:** Ideal for HR teams seeking to automate and standardize recruitment pipelines, reduce manual screening, and improve candidate quality.

### 2. HR & IT Helpdesk Chatbot with Audio Transcription
- **Purpose:** Deploys a chatbot that answers HR and IT policy questions using internal documents as a knowledge base.
- **Features:**
  - PDF document ingestion and parsing
  - Audio transcription for voice queries
  - Vector search for accurate, context-aware responses
  - Integration with Telegram for chat interface
  - OpenAI-powered embeddings and chat
- **Use Case:** Perfect for organizations wanting to provide instant, AI-driven support for HR/IT queries, leveraging their own policy documents.

### 3. CV Screening with OpenAI
- **Purpose:** Automates the initial screening of CVs for recruiters and HR professionals.
- **Features:**
  - Automated CV download and parsing (PDF/DOC)
  - Sends extracted data and job descriptions to OpenAI for analysis
  - Returns matching score, candidate summary, and suitability insights
  - Stores results in Supabase for further processing
- **Use Case:** Best for recruitment agencies and HR teams handling high volumes of applications, seeking to streamline and standardize candidate evaluation.

### 4. BambooHR AI-Powered Company Policies and Benefits Chatbot
- **Purpose:** Provides employees with instant answers to company policy and benefits questions using BambooHR data and internal documents.
- **Features:**
  - Integrates with BambooHR for real-time employee and policy data
  - Uses OpenAI and vector search for accurate, context-aware responses
  - Supports employee lookup and department-based queries
  - Handles multiple document types and knowledge sources
- **Use Case:** Suitable for companies using BambooHR who want to empower employees with self-service access to HR information and benefits.

---

## Getting Started
1. Import the desired JSON workflow(s) into your n8n instance.
2. Configure required credentials (OpenAI, Airtable, Supabase, BambooHR, etc.).
3. Adjust form fields, document sources, and notification settings as needed.
4. Deploy and test the workflows in your HR or IT environment.

---

## Why Use These Templates?
- **Save time:** Automate repetitive HR and recruitment tasks.
- **Improve accuracy:** Leverage AI for better candidate and employee support decisions.
- **Enhance experience:** Provide instant, 24/7 support for employees and applicants.
- **Easy integration:** Built for n8n, easily customizable and extensible.

---

## License
MIT 