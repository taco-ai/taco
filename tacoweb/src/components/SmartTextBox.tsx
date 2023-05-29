import React, { useState } from "react"

export interface SmartTextBoxProps {
    onUserInputComplete: (userInput: string) => void
}

export default function SmartTextBox(props: SmartTextBoxProps) {

    const [userInput, setUserInput] = useState<string>("")

    const onSubmit: React.FormEventHandler = async (event) => {
        props.onUserInputComplete(userInput)
        event.preventDefault()
    }

    const keyDownHandler: React.KeyboardEventHandler = async (event) => {
        if (event.key === 'Enter' && event.ctrlKey) {
            props.onUserInputComplete(userInput)
        }
    }

    const onChangeHandler: React.ChangeEventHandler<HTMLTextAreaElement> = async (event) => {
        setUserInput(event.target.value)
    }

    return (
        <form onSubmit={onSubmit} onKeyDown={keyDownHandler}>
            <textarea name="userInput"
                value={userInput}
                onChange={onChangeHandler}
            />
            <button>Submit</button>
        </form>
    )
}