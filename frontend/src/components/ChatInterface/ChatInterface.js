import {useState, useEffect} from 'react'
import axios from 'axios'
import io from 'socket.io-client'

const ChatInterface = () => {
    
    const [response, setResponse] = useState('')

    const [prompt, setPrompt] = useState('')




    const submit = () =>{
        // setResponse('')

        const socket = new WebSocket('ws://localhost:8000/ws/inference')

        socket.onopen = () => {
            // const prompt = "Write a python function to find prime numbers"
            socket.send(prompt)
        }

        socket.onmessage = (event) => {
            console.log(event)
            setResponse((prev) => prev + event.data)
        }

        socket.onclose = () => {
            console.log('WebSocket connection closed')
        }

    }
    

    return (
        <div>
            <h3> Response from LLM: </h3>
            <div style={{overflow:'auto', height:'70vh'}}>
                <pre>
                    {response}
                </pre>
            </div>
            
            <div style={{marginTop:'20vh'}}>
                <input
                style={{width: '20vw'}}
                value={prompt}
                onInput={e => setPrompt(e.target.value)}
                
                >
                
                </input>
                <button onClick={() => submit()}> Submit </button>

            </div>
        </div>
    )
}


export default ChatInterface;
