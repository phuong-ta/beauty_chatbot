document.addEventListener("DOMContentLoaded", function () {
    const chatBody = document.getElementById("chatBody");
    const userInput = document.getElementById("userInput");
    const sendButton = document.getElementById("sendButton");
    const loadingIcon = document.getElementById("loading");

    // Function to append user message to chat
    function appendUserMessage(message) {
        const userMessageDiv = document.createElement("div");
        userMessageDiv.classList.add("message", "user");
        userMessageDiv.innerHTML = `<span class="badge bg-primary">${message}</span>`;
        chatBody.appendChild(userMessageDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    // Function to append bot message to chat
    function appendBotMessage(message) {
        const botMessageDiv = document.createElement("div");
        botMessageDiv.classList.add("message", "bot");
        botMessageDiv.innerHTML = `<span class="badge bg-secondary">${message}</span>`;
        chatBody.appendChild(botMessageDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    }


    // Function to send message to sever, and get response sendMessageToServer
    async function sendMessageToServer(userMessage) {
        try {
            const response = await fetch('http://0.0.0.0:10000/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({message: userMessage})
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            return await response.json();
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            throw error;
        }
    }


    // simulateServerCommunication


    // Function to simulate server communication
    function simulateServerCommunication(userMessage) {
        // Show loading icon
        loadingIcon.style.display = "block";

        // Simulate waiting for a response (replace this with actual server communication)
        setTimeout(async () => {
            loadingIcon.style.display = "none";
            const botResponse = await sendMessageToServer(userMessage);
            // call function to send message to sever, add response to appendBotMessage

            //const botResponse = userMessage + " response"
            appendBotMessage("response "+ botResponse["message"]);
            console.log(botResponse);

        }, 1000);
    }

    // Handle send button click
    sendButton.addEventListener("click", function () {
        const userMessage = userInput.value.trim();
        if (userMessage === "") return;

        // Append user message to chat
        appendUserMessage(userMessage);

        // Clear input field
        userInput.value = "";

        // Send message to the server
        simulateServerCommunication(userMessage);
    });

    // Handle Enter key press for sending message
    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendButton.click();
        }
    });
});