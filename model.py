import boto3
import json


# define a function for the model
def transcriptActionExtractor(prompt_data):
    # initialize bedrock
    bedrock = boto3.client(service_name="bedrock-runtime")
    # instruction to model
    instructional_text = "From the meeting transcript above, Create a list of action items for each person."

    # define payload
    payload={
        "inputText": prompt_data + "\n" + instructional_text,
        "textGenerationConfig":{
            "maxTokenCount": 2048,
            "temperature": 0.6,
            "topP": 0.9
        }
        
    }

    # create body
    body = json.dumps(payload)
    # define model Amazaon Titan Text G1 Express in this case
    model_id = "amazon.titan-text-express-v1"

    # get response from the model
    response = bedrock.invoke_model(
        modelId = model_id,
        contentType = "application/json",
        accept = "application/json",
        body = body
    )
    # print response
    response_body = json.loads(response.get("body").read())
    output_text = response_body.get('results', [{}])[0].get('outputText', '')
    return output_text





