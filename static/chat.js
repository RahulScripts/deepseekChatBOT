
async function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    const chatHistory = document.getElementById('chatHistory');
    
    // Add user message
    chatHistory.innerHTML += `<div class="user-message">${userInput}</div>`;
    
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: userInput})
        });
        
        const data = await response.json();
        chatHistory.innerHTML += `<div class="assistant-message">${data.response}</div>`;
    } catch (error) {
        chatHistory.innerHTML += `<div class="error-message">${error}</div>`;
    }
    
    document.getElementById('userInput').value = '';
    chatHistory.scrollTop = chatHistory.scrollHeight;
}