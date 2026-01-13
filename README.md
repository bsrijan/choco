# Context

Sales reps of a distribution company are always on the go and they get phone calls from customers to place orders.

# Problems
- They have to pull over to take orders - note down details
- Turn on their laptop to record the order in the ERP system
- Tedious data entry and potential delays in relating data to internal teams like procurement to fulfil order

# Solution
- AI voice agent interfaces the customer to take corders - 24x7
- AI agent transcribes the conversation, summarizes it and makes the data available in a web app 
- manually review the order items and create a sales order in the ERP

# Techstack
- twilio
- eleven labs
- n8n
- flask
- mariadb
- vue.js
- aws

# How does the flow work?
- creates a US number in Twilio that a customer can call.
- wired the number with a voice agent in eleven labs.
- when the customer calls, the customer speaks to an AI agent to place the order
- created a webhook to relay conversational data from eleven lab to n8n.
- the data undergoes multiple transformations in n8n before pushing it to custom web app.
![image](https://github.com/user-attachments/assets/20ab129c-edff-422d-afd2-4360f22b8736)
- in the web app, a manual review of the order is needed before confirming the order in the system.

# Why is this solution better?
<br>

## Productivity
Realistically in the current state, the order throughput could be an estimated 2-3 orders per hour and with this solution, once could process 12 orders per hour - a 4x increase in productivity.
<br>
## Availability 
Unlike a human, AI agent can take orders 24/7 covering virtually any time zone.
<br>
## Traceablity 
Data including the call recording is available so there is highest level of transparency and accountability.
