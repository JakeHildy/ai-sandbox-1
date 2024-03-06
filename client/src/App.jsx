import { useState } from 'react';
import { Button, TextField, Container, Box } from '@mui/material';
import './App.css';
import axios from 'axios';
import Results from './components/Results.jsx'
import Example from './components/Example.jsx'

function App() {
    // State to hold the messages as an array of objects
    const [currentMessage, setCurrentMessage] = useState([]);
    // State to hold the current input
    const [responseObj, setResponseObj] = useState(null);

    // Function to handle the input change
    const handleInputChange = (event) => {
        setCurrentMessage(event.target.value);
    };

    // Function to handle form submit
    const handleSubmit = async (event) => {
        event.preventDefault();
        if (currentMessage.trim() !== '') {
            const response = await axios.post('http://localhost:3000', { prompt: currentMessage });
            const responseObj = JSON.parse(response.data.choices[0].message.content);
            setResponseObj(responseObj);
    }}

    return (
        <Container maxWidth="sm" sx={{border: '1px solid #e1e1e1;',  height: '100vh', width: '80vw', maxWidth: '1200px'}}>
            <Box sx={{ my: 4, display: 'flex', flexDirection: 'column', gap: 2, height: '40%'}}>
                <form onSubmit={handleSubmit}>
                    <Box
                        className="message-input"
                        sx={{ display: 'flex', gap: 1 }}
                    >
                        <TextField
                            fullWidth
                            label="Type a message..."
                            variant="outlined"
                            value={currentMessage}
                            onChange={handleInputChange}
                        />
                        <Button type="submit" variant="outlined">Send</Button>
                    </Box>
                </form>
                <Results responseObj={responseObj} />
                {/* <Example /> */}
            </Box>
        </Container>
    );
}

export default App
