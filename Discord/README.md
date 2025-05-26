# AI-Powered Discord Automation Templates for Content Sharing, Summarization, and Smart Routing with n8n

## Overview

This repository contains advanced n8n workflow templates designed to supercharge your Discord server with AI-driven automations. These templates enable seamless content sharing, intelligent message routing, and automated content summarization using OpenAI and other integrations. Whether you want to deliver daily comics, summarize YouTube videos, or triage user feedback, these workflows provide ready-to-use solutions that are easy to customize and extend.

---

## Included Workflows

### 1. Discord AI-powered Feedback Bot
- **Purpose:** Automatically categorizes user feedback using OpenAI (GPT-4) and routes it to the appropriate Discord channel (Success, IT, or Helpdesk) based on sentiment and urgency.
- **Features:**
  - Webhook and manual triggers
  - AI-powered message analysis and categorization
  - Smart routing to different Discord channels
  - Customizable categories and instructions

### 2. Daily Calvin and Hobbes Comics with AI Translation
- **Purpose:** Fetches the daily Calvin and Hobbes comic, uses AI to translate the dialogue into English and Korean (or another language), and posts both the comic and translations to Discord on a schedule.
- **Features:**
  - Scheduled daily execution
  - Web scraping and image extraction
  - AI-powered translation of comic dialogues
  - Automated posting to Discord

### 3. Share YouTube Videos with AI Summaries on Discord
- **Purpose:** Monitors a YouTube channel for new videos, retrieves captions, uses AI to summarize the content, and posts a summary and link to Discord.
- **Features:**
  - RSS feed trigger for new YouTube uploads
  - Caption retrieval and processing
  - AI-generated video summaries
  - Automated Discord posting with video link and summary

---

## Requirements
- [n8n](https://n8n.io/) (self-hosted or cloud)
- Discord Webhook URLs (for posting messages)
- [OpenAI API Key](https://platform.openai.com/) (for AI-powered features)
- YouTube Data API credentials (for YouTube workflow)

---

## Setup Instructions
1. **Clone or Download this Repository**
2. **Import Workflows into n8n:**
   - In n8n, go to "Workflows" > "Import from File" and select the desired JSON file.
3. **Configure Credentials:**
   - Set up your Discord Webhook, OpenAI, and YouTube credentials in n8n's credentials manager.
   - Update any placeholder webhook URLs or API keys in the workflow nodes.
4. **Customize as Needed:**
   - Adjust scheduling, translation languages, or message formats to fit your needs.
5. **Activate the Workflows:**
   - Enable the workflows in n8n to start automating!

---

## Customization Tips
- **Change Discord Channels:** Replace webhook URLs to post in different channels.
- **Modify AI Prompts:** Tweak the OpenAI prompts for different categorization or summary styles.
- **Add More Languages:** Extend translation steps for additional languages.
- **Expand Content Sources:** Adapt the YouTube or comic workflows for other sources.

---

## License
MIT

---

## Credits
- Inspired by the n8n community and open-source automation enthusiasts.
- Calvin and Hobbes comics © Bill Watterson / Andrews McMeel Syndication. 