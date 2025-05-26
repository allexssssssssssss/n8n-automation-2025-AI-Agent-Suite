# AI-Powered Database Automation Templates for n8n

## Intelligent Chat, Query Generation, and Data Management Across SQL, NoSQL, and Vector Databases

This repository contains a curated collection of advanced n8n workflow templates that leverage AI (OpenAI, LangChain) to enable intelligent, conversational, and automated interactions with a variety of databases. These templates are designed to help you build powerful, production-ready automations for querying, managing, and analyzing data across SQL, NoSQL, and vector databases—all through natural language chat interfaces and smart agents.

---

## 🚀 What's Included?

### 1. **Talk to your SQLite database with a LangChain AI Agent**
- **Description:** Chat with your SQLite database using a LangChain-powered AI agent. The workflow downloads a sample database, extracts it, and enables natural language queries with memory and context.
- **Use Case:** Quickly explore and analyze SQLite data conversationally.

### 2. **MongoDB AI Agent - Intelligent Movie Recommendations**
- **Description:** An AI agent that chats with users, queries a MongoDB movies collection using aggregation pipelines, and can insert favorite movies. Integrates OpenAI for natural language understanding.
- **Use Case:** Build smart recommendation systems or assistants for MongoDB datasets.

### 3. **Supabase Insertion & Upsertion & Retrieval**
- **Description:** End-to-end workflow for inserting, upserting, and retrieving data from a Supabase vector database, including embedding generation, retrieval, and deletion guidance. Includes setup notes for pgvector and custom SQL functions.
- **Use Case:** Manage and query vector data (e.g., for semantic search, AI apps) in Supabase.

### 4. **Chat with PostgreSQL Database**
- **Description:** Chatbot interface for PostgreSQL, powered by OpenAI and LangChain. Supports schema discovery, table definition, and custom SQL query execution, all via chat.
- **Use Case:** Conversational analytics and database management for PostgreSQL.

### 5. **Generate SQL queries from schema only - AI-powered**
- **Description:** AI agent generates SQL queries for a MySQL database using only the schema (no data access). Schema is extracted and cached for fast, secure query generation. The agent outputs queries for user execution.
- **Use Case:** Secure environments where only schema is available, or for teaching/learning SQL.

---

## ✨ Key Features
- **AI-Powered Chat:** Natural language interfaces for querying and managing databases.
- **Multi-Database Support:** SQLite, PostgreSQL, MySQL, MongoDB, and Supabase (vector DB).
- **Schema Extraction & Caching:** Fast, secure, and efficient query generation.
- **Memory & Context:** Multi-turn conversations with context retention.
- **Modular & Extensible:** Easily adapt templates for your own data and use cases.
- **Setup Guidance:** Sticky notes and comments in each workflow for easy onboarding.

---

## 🛠️ Setup & Usage
1. **Clone this repository** and open the workflows in n8n.
2. **Add your credentials** for the relevant database(s) and OpenAI API.
3. **Follow the sticky notes** in each workflow for setup steps (e.g., downloading sample data, enabling extensions, setting up tables/functions).
4. **Activate the workflow** and start chatting or running automations!

> **Tip:** Each workflow is self-documented with sticky notes and comments for quick onboarding.

---

## 📚 Extending & Customizing
- Swap out AI models or database nodes as needed.
- Add new triggers, actions, or integrations to fit your automation needs.
- Use as a foundation for building production-grade, AI-powered data tools.

---

## 🙏 Credits & References
- [n8n Documentation](https://docs.n8n.io/)
- [LangChain](https://langchain.com/)
- [OpenAI](https://openai.com/)
- [Supabase](https://supabase.com/)
- [MongoDB](https://www.mongodb.com/)
- [Chinook Sample Database](https://www.sqlitetutorial.net/sqlite-sample-database/)

---

**Unleash the power of AI-driven database automation with these ready-to-use n8n templates!** 