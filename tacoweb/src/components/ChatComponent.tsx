import React, { useEffect, useState } from "react"
import SmartTextBox from "./SmartTextBox"

export default function ChatComponent() {

    const [messages, setMessages] = useState<string[]>([])
    const [isUserPromptComplete, setUserPromptComplete] = useState<boolean>(false)

    const uppdateMessages = async (userPrompt: string) => {
        setMessages([...messages, userPrompt])
        setUserPromptComplete(true)
    }

    useEffect(() => {
        // run this on every repaint.
        console.log("repaint!")
        console.log(`${isUserPromptComplete}`)
        if(isUserPromptComplete) {
            console.log("user Prompt is complete - need to ask backend for response")
        }
    })

    return (<>
        {messages.map(m => {
            return (<div key={m}> User: {m} </div>)
        })}
        <div>
            {!isUserPromptComplete && <SmartTextBox onUserInputComplete={uppdateMessages} />}
        </div>
    </>)
}