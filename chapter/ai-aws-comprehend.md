# Amazon Comprehend on AWS sp20-516-227 Xin Gu

### Intro

Amazon Comprehensive gives insights based on analyzing text materials by Natural Language Processing (NLP). It could identify the languages, entities, make relations with terms or topics, detect the sentiment. Amazon Comprehensive can be customized to find specific words or phrases of interests, such as membership, cancellation or part codes [@227comprehendf]. 

@fig:AWScomprehend shows the workflow of Amazon Comprehend. 

![Amazon Comprehend Working Mechanism](images/AWScomprehend.png){#fig:AWScomprehend}

Amazon Comprehend Medical is specific for better extracting information from medical notes or reports. It can accurately draw information from complex and various types of medical terms, such as dosages, strengths, frequencies, and medications. Amazon Comprehend Medical can connect related medications with dosages, strengths, and frequencies.

##### Features

    * Keyphrase Extraction
    * Sentiment Analysis
    * Syntax Analysis
    * Entity Recognition
    * Comprehend Medical
        - Medical Named Entity and Relationship Extraction (NERe)
        - Medical Ontology Linking
    * Custom Entities
    * Language Detection
        - Amazon Comprehend chould detect 100 different kinds of languages. The output is about the domain language with a amazon confidence score.
    * Custom Classification
    * Topic Modeling
    * Multiple language support
        - Other than detect domine languge, More features are offered for 12 languages, including German, Italian, Japanese, Arabic, English, Portuguese, Korean, Chinese (simplified), Spanish, French, Hindi, and Chinese (traditional).

##### Pricing

The machine learning model was pre-trained; users do not need to know how to do machine learning, train their model, nor deploy it. AWS fully manages the service, and users only pay for what they used base on the amount of text. 

The Amazon Comprehensive free tier is available for AWS customers for 12 months, starting from the time requiring the Amazon Comprehensive service [@277comprehendpricing].

#### Amazon Comprehend Console

##### Login to Amazon Comprehend Console

Login to your Amazon AWS account, search for "comprehend", open the web page <https://console.aws.amazon.com/comprehend/home?region=us-east-1#welcome> for Amazon Comprehend, click "Launch Amazon comprehend", shown in @fig:227AWSComLogin. 

![Launch Amazon Comprehend](images/AWSComLogin.png){#fig:227AWSComLogin}

In Amazon Comprehend Console, you can analyze text with up to 1000 words. Click "Analyze" to run an analyze of the text.

##### Analysis with Amazon Comprehend Console

Take a short paragrah from an article online [@Verhoeven2020Feb] about travling in vietman as an example. @fig:227AWSComEnti show the analysis result of entities.

![Analysis Result about Entities in Text](images/AWSComEnti.png){#fig:227AWSComEnti}

Result table shows identified words, categories confidence scores in each column. For this example, AWS comprehend successfully identified vietnaness location names.

There are 

#### Amazon Command Line Interface

Please refer to [Cloud Computing](https://laszewski.github.io/book/cloud/), 9.2.4 AWS Command Line Interface.

To get more information about installing Amazon CLI, please see the [link](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).


### Text Analysis APIs

#### Detect the Dominant Language

 

#### Detect Entities

#### Detect Key Phrases

#### Determine Sentiment

#### Analyze Syntax

#### Topic Modeling

### Examples



### Architecture

image: AWS solution architecture

### Use Cases

* <https://aws.amazon.com/machine-learning/ai-services/>

```bash
aws iam create-group --group-name Admins
```