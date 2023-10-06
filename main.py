# Import the openai library
import openai

# Set your OpenAI API key
openai.api_key = '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'


# Define a function to get a response from the GPT-3 model based on a given prompt
def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        # Create a completion using the GPT-3 model
        response: dict = openai.Completion.create(
            model='text-davinci-003',  # Specify the model you want to use
            prompt=prompt,  # Pass the user's prompt as input
            temperature=0.7,  # Adjust the temperature for randomness (0.7 is moderately random)
            max_tokens=150,  # Set a maximum token limit for the response
            top_p=1,  # Control the diversity of responses
            frequency_penalty=0,  # Penalize frequent tokens (set to 0 for no penalty)
            presence_penalty=0.6,  # Penalize infrequent tokens (adjust as needed)
            stop=['\n']  # Specify tokens at which the response should stop
        )

        # Extract the first choice (response) from the API response
        choices: dict = response.choices[0]
        text = choices.get('text')
    except Exception as e:
        # Handle any exceptions that may occur during the API call
        print('Error', e)

    # Return the generated text or None if there was an error
    return text


# Define a function to create a prompt by combining the user's input with the bot's response
def create_prompt(message: str) -> str:
    # Create a prompt that combines user input with conversation history
    return f'You: {message}\nBot:'


# Define the main function to handle user interaction
def main():
    # Initialize the conversation with an introductory message
    conversation: str = 'The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.'

    while True:
        # Get user input
        user_input: str = input('You: ')

        # Check if user input is not empty
        if user_input.strip():
            # Create a prompt with the user's input and conversation history
            prompt: str = create_prompt(user_input)

            # Get the bot's response based on the prompt and conversation history
            bot_response: str = get_api_response(prompt)

            # Print the bot's response
            print(f'Bot: {bot_response}')

            # Update the conversation history with the user's input and bot's response
            conversation += f' {user_input}\nBot: {bot_response}'


# Run the main function when the script is executed
if __name__ == '__main__':
    main()
