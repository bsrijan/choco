context:
sales reps of a distribution company are always on the go and they get customer phone calls to place an order.

problems:
- they have to pull over to take orders - note down details
- turn on their laptop to record the order in the ERP system
- tedious data entry and potential delays in relating data to internal teams like procurement to fulfil order

solution:
- AI voice agent interfaces the customer to take corders - 24x7
- AI agent transcribes the conversation, summarizes it and makes the data available in a web app 
- manually review the order items and create a sales order in the ERP

techstack:
- twilio
- eleven labs
- n8n
- flask
- mariadb
- vue.js
- aws

how does the flow work?
- created a US number in Twilio that a customer can call.
- wired the number with a voice agent in eleven labs
- when the customer calls, the customer speaks to an AI agent to place the order
- created a webhook to relay conversational data from eleven lab to n8n
- the data undergoes multiple transformations in n8n before pushing it to custom web app