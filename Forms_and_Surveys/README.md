# AI-Enhanced Forms & Surveys Automation Templates for n8n

A collection of advanced n8n workflow templates that leverage AI, multi-step forms, and integrations (Airtable, Google Calendar, Gmail, Redis) to automate appointment scheduling, email subscription management, and conversational interviews. These templates are designed for seamless user experiences, smart data handling, and scalable automation.

## Templates Included

### 1. AI-Qualified Appointment Scheduling
- Multi-step forms for onboarding, terms acceptance, and date/time selection
- AI-powered enquiry filtering (OpenAI integration)
- Admin approval workflow via email
- Google Calendar integration for confirmed appointments
- Automated email notifications for acceptance/rejection
- User-friendly, split-form experience for better engagement

### 2. Automated Email Subscription Service
- User subscriptions via n8n forms
- Content generation with AI
- Airtable backend for managing subscribers and schedules
- Automated email delivery and unsubscribe flow
- Logging and analytics via Airtable

### 3. Conversational AI Interviews
- AI agent dynamically generates and asks interview questions
- User answers are recorded in a session (using Redis for storage)
- Loop continues until the user ends the interview
- Final transcript is displayed or stored for analysis
- Designed for scalable, asynchronous user research

## Key Features
- Multi-step, user-friendly forms for data collection and onboarding
- AI integration for smart qualification and content generation
- Scalable backend integrations (Airtable, Redis, Google Calendar, Gmail)
- Automated notifications and approval flows
- Ready-to-use, easily customizable n8n JSON templates

## How to Use
1. Import the desired JSON file(s) into your n8n instance.
2. Configure credentials for any required integrations (OpenAI, Gmail, Airtable, Google Calendar, Redis).
3. Customize form fields, messages, and logic as needed.
4. Deploy and enjoy automated, AI-powered workflows! 