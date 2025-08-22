---
layout: default
title: "Threats in AI/ML Models"
parent: Sonatype IQ Server
nav_order: 11
---

# Threats in AI/ML Models

*Sonatype Lifecycle* can detect malware, vulnerabilities and license obligations within AI/ML models downloaded from the Hugging Face repository. These capabilities are continuously evolving to stay in sync with the rapidly changing open-source AI/ML technology landscape. Please check release notes for the latest enhancements to our AI/ML threat protection capabilities.

## Risks with AI/ML Components

AI/ML components are reusable building blocks generally written in Python, C++, Java, Go(Golang) that contribute directly to the functionality of an AI/ML system. These functionalities include:

- Data pre-processing for data cleaning, transformation, and feature engineering.
- Data pre-processing for data cleaning, transformation, and feature engineering.
- Model evaluation to assess the performance of trained ML models based on accuracy and effectiveness.
- Inference components that deploy the trained models to new data.
- Natural Language Processing (NLP) components that handle text analysis, sentiment analysis and language translations.
- Computer Vision components that see or interpret images for object or image recognition.

*Sonatype Lifecycle* with its comprehensive coordinate matching [policy constraints](#UUID-39d840f0-d51b-c09b-8272-415acbc57462) can detect most vulnerabilities affecting these components during policy evaluations. It provides protection against [security](#UUID-6caa3d47-20de-8dd2-f544-0dafd09e4b2c_section-idm234860151231854) , [legal](#UUID-6caa3d47-20de-8dd2-f544-0dafd09e4b2c_section-idm234860153743091) and [quality](#UUID-6caa3d47-20de-8dd2-f544-0dafd09e4b2c_section-idm234860155726784) risks.

## AI/ML Security Risk

*Sonatype Lifecycle* can help identify open-source AI/ML libraries of a wide range of formats on Hugging Face, for e.g. Pytorch with extensions `.bin` , `.pt` , `.pkl` , `.pickle` . Additionally, our Security Research team identifies models that execute malicious code, have been built with poisoned data sets, and other model related vulnerabilities.

### Usage Scenario

In addition to having traditional security policies driven by a vulnerability's severity, AppSec teams can create security policies designed to detect pickle files that can execute arbitrary code, create new processes or establish networking capabilities, during the de-serialization process.Lifecycle’s analysis at each DevOps stage ensures that the same (identical) model that has been cleared for use is being used for development.

[See table for a complete list of supported formats and extensions](https://help.sonatype.com/en/hugging-face-model-analysis.html) .

## AI/ML Legal Risk

*Sonatype Lifecycle* and Advanced Legal Pack (ALP) can detect and manage license attributions and obligations by providing detailed information on effective, declared, and observed licenses for open-source AI/ML models on Hugging Face. Additionally, Lifecycle and ALP provide legal coverage for obligations that are specific to AI/ML models like “restriction on use of output to train other models” or “restriction on use of output for commercial purposes”.

### Usage Scenario

Open source governance teams can ensure, through license policies, that AI models meet organization guidelines and are acceptable for use.

## AI/ML Quality Risk

Architects and AppSec teams can create policy to ensure that the models being used by data science or development meet certain quality criteria. For instance, Lifecycle supports policy on if the model is [Foundation or derivative](#UUID-6caa3d47-20de-8dd2-f544-0dafd09e4b2c_section-idm234832704377338) , or contains [Objectionable Content](#UUID-6caa3d47-20de-8dd2-f544-0dafd09e4b2c_N1748445288080) .

Having these policies in place can be used to automate many of the gates otherwise required before adopting a model.

## AI/ML Derivative Model Detection

Data scientists and data engineers often encounter the need to retrain an existing open-source model to enhance the accuracy or adjust a "drift" in the performance of a model. They can tweak a Foundation Model by retraining or fine-tuning it on different data sets, adjusting weights, features and hyper-parameters.

An AI/ML derivative model is a tweaked version derived from a Foundation Model.

Such derivative AI/ML models are also hosted in Hugging Face repositories. However, the derivative models may not have the exact same license restrictions and obligations as the Foundation Model. They may not be proven, or vetted for the organization's business case.

The " [Derivative AI Model](#UUID-39d840f0-d51b-c09b-8272-415acbc57462) " policy condition allows users to set a policy to check the lineage of the AI model being used in the application. The policy evaluation will report a violation if a derivative model is used. The report will include the name of corresponding Foundation Model.

The " [Derivative AI Model](#UUID-39d840f0-d51b-c09b-8272-415acbc57462) " condition can also be used to establish provenance by ensuring that the exact same AI model that has been approved for use is actually being used in the application. This will ensure that other derived AI models which may be compromised or do not satisfy the accuracy and relevance requirements of the organization's needs, do not enter the development pipelines.

## Objectionable AI Detection

As part of efforts to promote Responsible AI, models are reviewed for content that include offensive and demeaning language that could lead to hostile or alienating environments for people belonging to a specific gender, race, nationality or identifying with other physical/psychological human factors.

Such models violate the organizational content policy and are tagged as *Objectionable* . Sonatype Component Intelligence team reviews if the model is tagged as Not For All Audiences (by Hugging Face) or NSFW (Not Safe For Work) as reported by the creator of the model/repository, or whether the model/repository contains banned terms/phrases in its name or in Readme.

The " [AI Content" policy condition](https://help.sonatype.com/en/policy-constraints.html#idp280435) allows users to set a policy to check if the model is tagged as Objectionable AI. The policy evaluation will report a violation if an AI model tagged as *Objectionable* is used.
