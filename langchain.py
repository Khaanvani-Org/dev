
import langchain
{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JRpULjNO8oRD",
        "outputId": "cfce9af3-0f81-4fba-8ca0-d4fc5dd07031"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: langchain==0.0.279 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (0.0.279)\n",
            "Requirement already satisfied: PyYAML>=5.3 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (6.0)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (1.4.39)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (3.8.3)\n",
            "Requirement already satisfied: dataclasses-json<0.6.0,>=0.5.7 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (0.5.14)\n",
            "Requirement already satisfied: langsmith<0.1.0,>=0.0.21 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (0.0.41)\n",
            "Requirement already satisfied: numexpr<3.0.0,>=2.8.4 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (2.8.4)\n",
            "Requirement already satisfied: numpy<2,>=1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (1.24.3)\n",
            "Requirement already satisfied: pydantic<3,>=1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (1.10.12)\n",
            "Requirement already satisfied: requests<3,>=2 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (2.31.0)\n",
            "Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from langchain==0.0.279) (8.2.2)\n",
            "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.279) (22.1.0)\n",
            "Requirement already satisfied: charset-normalizer<3.0,>=2.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.279) (2.0.4)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.279) (6.0.2)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.279) (4.0.2)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.279) (1.8.1)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.279) (1.3.3)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.279) (1.2.0)\n",
            "Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain==0.0.279) (3.20.1)\n",
            "Requirement already satisfied: typing-inspect<1,>=0.4.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain==0.0.279) (0.9.0)\n",
            "Requirement already satisfied: typing-extensions>=4.2.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pydantic<3,>=1->langchain==0.0.279) (4.7.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain==0.0.279) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain==0.0.279) (1.26.16)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain==0.0.279) (2023.7.22)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from SQLAlchemy<3,>=1.4->langchain==0.0.279) (2.0.1)\n",
            "Requirement already satisfied: packaging>=17.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from marshmallow<4.0.0,>=3.18.0->dataclasses-json<0.6.0,>=0.5.7->langchain==0.0.279) (23.0)\n",
            "Requirement already satisfied: mypy-extensions>=0.3.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.6.0,>=0.5.7->langchain==0.0.279) (0.4.3)\n",
            "Note: you may need to restart the kernel to use updated packages.\n",
            "Requirement already satisfied: openai==0.27.5 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (0.27.5)\n",
            "Requirement already satisfied: requests>=2.20 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from openai==0.27.5) (2.31.0)\n",
            "Requirement already satisfied: tqdm in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from openai==0.27.5) (4.65.0)\n",
            "Requirement already satisfied: aiohttp in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from openai==0.27.5) (3.8.3)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.27.5) (2.0.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.27.5) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.27.5) (1.26.16)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.27.5) (2023.7.22)\n",
            "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.27.5) (22.1.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.27.5) (6.0.2)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.27.5) (4.0.2)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.27.5) (1.8.1)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.27.5) (1.3.3)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.27.5) (1.2.0)\n",
            "Requirement already satisfied: colorama in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from tqdm->openai==0.27.5) (0.4.6)\n",
            "Note: you may need to restart the kernel to use updated packages.\n"
          ]
        }
      ],
      "source": [
        "%pip install langchain==0.0.279\n",
        "%pip install openai==0.27.5"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VCxwb2wN9L0x",
        "outputId": "8ff568a7-8e70-48a7-c1ca-4d4595d1e96c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: sentence_transformers in c:\\users\\pruth\\anaconda3\\lib\\site-packages (2.2.2)\n",
            "Requirement already satisfied: transformers<5.0.0,>=4.6.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (4.34.0)\n",
            "Requirement already satisfied: tqdm in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (4.65.0)\n",
            "Requirement already satisfied: torch>=1.6.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (2.1.0)\n",
            "Requirement already satisfied: torchvision in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (0.16.0)\n",
            "Requirement already satisfied: numpy in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (1.24.3)\n",
            "Requirement already satisfied: scikit-learn in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (1.3.0)\n",
            "Requirement already satisfied: scipy in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (1.10.1)\n",
            "Requirement already satisfied: nltk in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (3.8.1)\n",
            "Requirement already satisfied: sentencepiece in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (0.1.99)\n",
            "Requirement already satisfied: huggingface-hub>=0.4.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sentence_transformers) (0.17.3)\n",
            "Requirement already satisfied: filelock in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.4.0->sentence_transformers) (3.9.0)\n",
            "Requirement already satisfied: fsspec in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.4.0->sentence_transformers) (2023.3.0)\n",
            "Requirement already satisfied: requests in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.4.0->sentence_transformers) (2.31.0)\n",
            "Requirement already satisfied: pyyaml>=5.1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.4.0->sentence_transformers) (6.0)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.4.0->sentence_transformers) (4.7.1)\n",
            "Requirement already satisfied: packaging>=20.9 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.4.0->sentence_transformers) (23.0)\n",
            "Requirement already satisfied: sympy in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from torch>=1.6.0->sentence_transformers) (1.11.1)\n",
            "Requirement already satisfied: networkx in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from torch>=1.6.0->sentence_transformers) (3.1)\n",
            "Requirement already satisfied: jinja2 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from torch>=1.6.0->sentence_transformers) (3.1.2)\n",
            "Requirement already satisfied: colorama in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from tqdm->sentence_transformers) (0.4.6)\n",
            "Requirement already satisfied: regex!=2019.12.17 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from transformers<5.0.0,>=4.6.0->sentence_transformers) (2022.7.9)\n",
            "Requirement already satisfied: tokenizers<0.15,>=0.14 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from transformers<5.0.0,>=4.6.0->sentence_transformers) (0.14.1)\n",
            "Requirement already satisfied: safetensors>=0.3.1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from transformers<5.0.0,>=4.6.0->sentence_transformers) (0.4.0)\n",
            "Requirement already satisfied: click in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from nltk->sentence_transformers) (8.1.7)\n",
            "Requirement already satisfied: joblib in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from nltk->sentence_transformers) (1.2.0)\n",
            "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from scikit-learn->sentence_transformers) (2.2.0)\n",
            "Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from torchvision->sentence_transformers) (9.4.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from jinja2->torch>=1.6.0->sentence_transformers) (2.1.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests->huggingface-hub>=0.4.0->sentence_transformers) (2.0.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests->huggingface-hub>=0.4.0->sentence_transformers) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests->huggingface-hub>=0.4.0->sentence_transformers) (1.26.16)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests->huggingface-hub>=0.4.0->sentence_transformers) (2023.7.22)\n",
            "Requirement already satisfied: mpmath>=0.19 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from sympy->torch>=1.6.0->sentence_transformers) (1.3.0)\n",
            "Note: you may need to restart the kernel to use updated packages.\n"
          ]
        }
      ],
      "source": [
        "%pip install sentence_transformers"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pPtc2U-M9aVO",
        "outputId": "552d9ebc-f955-4c8e-c874-fff47aa4f79b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Note: you may need to restart the kernel to use updated packages.\n",
            "Note: you may need to restart the kernel to use updated packages.\n",
            "Note: you may need to restart the kernel to use updated packages.\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "  error: subprocess-exited-with-error\n",
            "  \n",
            "  × python setup.py bdist_wheel did not run successfully.\n",
            "  │ exit code: 1\n",
            "  ╰─> [353 lines of output]\n",
            "      running bdist_wheel\n",
            "      c:\\Users\\pruth\\anaconda3\\Lib\\site-packages\\torch\\utils\\cpp_extension.py:502: UserWarning: Attempted to use ninja as the BuildExtension backend but we could not find ninja.. Falling back to using the slow distutils backend.\n",
            "        warnings.warn(msg.format('we could not find ninja.'))\n",
            "      running build\n",
            "      running build_py\n",
            "      creating build\n",
            "      creating build\\lib.win-amd64-cpython-311\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\n",
            "      copying detectron2\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\n",
            "      creating build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\analyze_model.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\benchmark.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\convert-torchvision-to-d2.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\lazyconfig_train_net.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\lightning_train_net.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\plain_train_net.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\train_net.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\visualize_data.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\visualize_json_results.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      copying tools\\__init__.py -> build\\lib.win-amd64-cpython-311\\tools\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\checkpoint\n",
            "      copying detectron2\\checkpoint\\c2_model_loading.py -> build\\lib.win-amd64-cpython-311\\detectron2\\checkpoint\n",
            "      copying detectron2\\checkpoint\\catalog.py -> build\\lib.win-amd64-cpython-311\\detectron2\\checkpoint\n",
            "      copying detectron2\\checkpoint\\detection_checkpoint.py -> build\\lib.win-amd64-cpython-311\\detectron2\\checkpoint\n",
            "      copying detectron2\\checkpoint\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\checkpoint\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\config\n",
            "      copying detectron2\\config\\compat.py -> build\\lib.win-amd64-cpython-311\\detectron2\\config\n",
            "      copying detectron2\\config\\config.py -> build\\lib.win-amd64-cpython-311\\detectron2\\config\n",
            "      copying detectron2\\config\\defaults.py -> build\\lib.win-amd64-cpython-311\\detectron2\\config\n",
            "      copying detectron2\\config\\instantiate.py -> build\\lib.win-amd64-cpython-311\\detectron2\\config\n",
            "      copying detectron2\\config\\lazy.py -> build\\lib.win-amd64-cpython-311\\detectron2\\config\n",
            "      copying detectron2\\config\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\config\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\data\n",
            "      copying detectron2\\data\\benchmark.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\n",
            "      copying detectron2\\data\\build.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\n",
            "      copying detectron2\\data\\catalog.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\n",
            "      copying detectron2\\data\\common.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\n",
            "      copying detectron2\\data\\dataset_mapper.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\n",
            "      copying detectron2\\data\\detection_utils.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\n",
            "      copying detectron2\\data\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\engine\n",
            "      copying detectron2\\engine\\defaults.py -> build\\lib.win-amd64-cpython-311\\detectron2\\engine\n",
            "      copying detectron2\\engine\\hooks.py -> build\\lib.win-amd64-cpython-311\\detectron2\\engine\n",
            "      copying detectron2\\engine\\launch.py -> build\\lib.win-amd64-cpython-311\\detectron2\\engine\n",
            "      copying detectron2\\engine\\train_loop.py -> build\\lib.win-amd64-cpython-311\\detectron2\\engine\n",
            "      copying detectron2\\engine\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\engine\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\cityscapes_evaluation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\coco_evaluation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\evaluator.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\fast_eval_api.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\lvis_evaluation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\panoptic_evaluation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\pascal_voc_evaluation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\rotated_coco_evaluation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\sem_seg_evaluation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\testing.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      copying detectron2\\evaluation\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\evaluation\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\api.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\c10.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\caffe2_export.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\caffe2_inference.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\caffe2_modeling.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\caffe2_patch.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\flatten.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\shared.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\torchscript.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\torchscript_patch.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      copying detectron2\\export\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\export\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\aspp.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\batch_norm.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\blocks.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\deform_conv.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\losses.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\mask_ops.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\nms.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\roi_align.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\roi_align_rotated.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\rotated_boxes.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\shape_spec.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\wrappers.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      copying detectron2\\layers\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\layers\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      copying detectron2\\modeling\\anchor_generator.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      copying detectron2\\modeling\\box_regression.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      copying detectron2\\modeling\\matcher.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      copying detectron2\\modeling\\mmdet_wrapper.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      copying detectron2\\modeling\\poolers.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      copying detectron2\\modeling\\postprocessing.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      copying detectron2\\modeling\\sampling.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      copying detectron2\\modeling\\test_time_augmentation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      copying detectron2\\modeling\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\n",
            "      copying detectron2\\model_zoo\\model_zoo.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\n",
            "      copying detectron2\\model_zoo\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\projects\n",
            "      copying detectron2\\projects\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\solver\n",
            "      copying detectron2\\solver\\build.py -> build\\lib.win-amd64-cpython-311\\detectron2\\solver\n",
            "      copying detectron2\\solver\\lr_scheduler.py -> build\\lib.win-amd64-cpython-311\\detectron2\\solver\n",
            "      copying detectron2\\solver\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\solver\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\structures\n",
            "      copying detectron2\\structures\\boxes.py -> build\\lib.win-amd64-cpython-311\\detectron2\\structures\n",
            "      copying detectron2\\structures\\image_list.py -> build\\lib.win-amd64-cpython-311\\detectron2\\structures\n",
            "      copying detectron2\\structures\\instances.py -> build\\lib.win-amd64-cpython-311\\detectron2\\structures\n",
            "      copying detectron2\\structures\\keypoints.py -> build\\lib.win-amd64-cpython-311\\detectron2\\structures\n",
            "      copying detectron2\\structures\\masks.py -> build\\lib.win-amd64-cpython-311\\detectron2\\structures\n",
            "      copying detectron2\\structures\\rotated_boxes.py -> build\\lib.win-amd64-cpython-311\\detectron2\\structures\n",
            "      copying detectron2\\structures\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\structures\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\analysis.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\collect_env.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\colormap.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\comm.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\env.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\events.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\file_io.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\logger.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\memory.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\registry.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\serialize.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\testing.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\video_visualizer.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\visualizer.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      copying detectron2\\utils\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\utils\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\builtin.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\builtin_meta.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\cityscapes.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\cityscapes_panoptic.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\coco.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\coco_panoptic.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\lvis.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\lvis_v0_5_categories.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\lvis_v1_categories.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\pascal_voc.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\register_coco.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      copying detectron2\\data\\datasets\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\datasets\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\data\\samplers\n",
            "      copying detectron2\\data\\samplers\\distributed_sampler.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\samplers\n",
            "      copying detectron2\\data\\samplers\\grouped_batch_sampler.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\samplers\n",
            "      copying detectron2\\data\\samplers\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\samplers\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\data\\transforms\n",
            "      copying detectron2\\data\\transforms\\augmentation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\transforms\n",
            "      copying detectron2\\data\\transforms\\augmentation_impl.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\transforms\n",
            "      copying detectron2\\data\\transforms\\transform.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\transforms\n",
            "      copying detectron2\\data\\transforms\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\data\\transforms\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\backbone\n",
            "      copying detectron2\\modeling\\backbone\\backbone.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\backbone\n",
            "      copying detectron2\\modeling\\backbone\\build.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\backbone\n",
            "      copying detectron2\\modeling\\backbone\\fpn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\backbone\n",
            "      copying detectron2\\modeling\\backbone\\regnet.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\backbone\n",
            "      copying detectron2\\modeling\\backbone\\resnet.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\backbone\n",
            "      copying detectron2\\modeling\\backbone\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\backbone\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\meta_arch\n",
            "      copying detectron2\\modeling\\meta_arch\\build.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\meta_arch\n",
            "      copying detectron2\\modeling\\meta_arch\\dense_detector.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\meta_arch\n",
            "      copying detectron2\\modeling\\meta_arch\\fcos.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\meta_arch\n",
            "      copying detectron2\\modeling\\meta_arch\\panoptic_fpn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\meta_arch\n",
            "      copying detectron2\\modeling\\meta_arch\\rcnn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\meta_arch\n",
            "      copying detectron2\\modeling\\meta_arch\\retinanet.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\meta_arch\n",
            "      copying detectron2\\modeling\\meta_arch\\semantic_seg.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\meta_arch\n",
            "      copying detectron2\\modeling\\meta_arch\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\meta_arch\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\proposal_generator\n",
            "      copying detectron2\\modeling\\proposal_generator\\build.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\proposal_generator\n",
            "      copying detectron2\\modeling\\proposal_generator\\proposal_utils.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\proposal_generator\n",
            "      copying detectron2\\modeling\\proposal_generator\\rpn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\proposal_generator\n",
            "      copying detectron2\\modeling\\proposal_generator\\rrpn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\proposal_generator\n",
            "      copying detectron2\\modeling\\proposal_generator\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\proposal_generator\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\roi_heads\n",
            "      copying detectron2\\modeling\\roi_heads\\box_head.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\roi_heads\n",
            "      copying detectron2\\modeling\\roi_heads\\cascade_rcnn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\roi_heads\n",
            "      copying detectron2\\modeling\\roi_heads\\fast_rcnn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\roi_heads\n",
            "      copying detectron2\\modeling\\roi_heads\\keypoint_head.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\roi_heads\n",
            "      copying detectron2\\modeling\\roi_heads\\mask_head.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\roi_heads\n",
            "      copying detectron2\\modeling\\roi_heads\\roi_heads.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\roi_heads\n",
            "      copying detectron2\\modeling\\roi_heads\\rotated_fast_rcnn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\roi_heads\n",
            "      copying detectron2\\modeling\\roi_heads\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\modeling\\roi_heads\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\projects\\point_rend\n",
            "      copying projects\\PointRend\\point_rend\\color_augmentation.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\point_rend\n",
            "      copying projects\\PointRend\\point_rend\\config.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\point_rend\n",
            "      copying projects\\PointRend\\point_rend\\mask_head.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\point_rend\n",
            "      copying projects\\PointRend\\point_rend\\point_features.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\point_rend\n",
            "      copying projects\\PointRend\\point_rend\\point_head.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\point_rend\n",
            "      copying projects\\PointRend\\point_rend\\roi_heads.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\point_rend\n",
            "      copying projects\\PointRend\\point_rend\\semantic_seg.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\point_rend\n",
            "      copying projects\\PointRend\\point_rend\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\point_rend\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\projects\\deeplab\n",
            "      copying projects\\DeepLab\\deeplab\\build_solver.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\deeplab\n",
            "      copying projects\\DeepLab\\deeplab\\config.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\deeplab\n",
            "      copying projects\\DeepLab\\deeplab\\loss.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\deeplab\n",
            "      copying projects\\DeepLab\\deeplab\\lr_scheduler.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\deeplab\n",
            "      copying projects\\DeepLab\\deeplab\\resnet.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\deeplab\n",
            "      copying projects\\DeepLab\\deeplab\\semantic_seg.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\deeplab\n",
            "      copying projects\\DeepLab\\deeplab\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\deeplab\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\projects\\panoptic_deeplab\n",
            "      copying projects\\Panoptic-DeepLab\\panoptic_deeplab\\config.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\panoptic_deeplab\n",
            "      copying projects\\Panoptic-DeepLab\\panoptic_deeplab\\dataset_mapper.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\panoptic_deeplab\n",
            "      copying projects\\Panoptic-DeepLab\\panoptic_deeplab\\panoptic_seg.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\panoptic_deeplab\n",
            "      copying projects\\Panoptic-DeepLab\\panoptic_deeplab\\post_processing.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\panoptic_deeplab\n",
            "      copying projects\\Panoptic-DeepLab\\panoptic_deeplab\\target_generator.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\panoptic_deeplab\n",
            "      copying projects\\Panoptic-DeepLab\\panoptic_deeplab\\__init__.py -> build\\lib.win-amd64-cpython-311\\detectron2\\projects\\panoptic_deeplab\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\n",
            "      copying detectron2\\model_zoo\\configs\\Base-RCNN-C4.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\n",
            "      copying detectron2\\model_zoo\\configs\\Base-RCNN-DilatedC5.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\n",
            "      copying detectron2\\model_zoo\\configs\\Base-RCNN-FPN.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\n",
            "      copying detectron2\\model_zoo\\configs\\Base-RetinaNet.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Cityscapes\n",
            "      copying detectron2\\model_zoo\\configs\\Cityscapes\\mask_rcnn_R_50_FPN.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Cityscapes\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_R_101_C4_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_R_101_DC5_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_R_101_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_R_50_C4_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_R_50_C4_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_R_50_DC5_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_R_50_DC5_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_R_50_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\faster_rcnn_X_101_32x8d_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\fast_rcnn_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\retinanet_R_101_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\retinanet_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\retinanet_R_50_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\rpn_R_50_C4_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\rpn_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_101_C4_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_101_DC5_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_101_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_50_C4_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_50_C4_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_50_DC5_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_50_DC5_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_50_FPN_1x_giou.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_50_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_X_101_32x8d_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Keypoints\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Keypoints\\Base-Keypoint-RCNN-FPN.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Keypoints\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Keypoints\\keypoint_rcnn_R_101_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Keypoints\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Keypoints\\keypoint_rcnn_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Keypoints\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Keypoints\\keypoint_rcnn_R_50_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Keypoints\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Keypoints\\keypoint_rcnn_X_101_32x8d_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Keypoints\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\\Base-Panoptic-FPN.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\\panoptic_fpn_R_101_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\\panoptic_fpn_R_50_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\\panoptic_fpn_R_50_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Detectron1-Comparisons\n",
            "      copying detectron2\\model_zoo\\configs\\Detectron1-Comparisons\\faster_rcnn_R_50_FPN_noaug_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Detectron1-Comparisons\n",
            "      copying detectron2\\model_zoo\\configs\\Detectron1-Comparisons\\keypoint_rcnn_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Detectron1-Comparisons\n",
            "      copying detectron2\\model_zoo\\configs\\Detectron1-Comparisons\\mask_rcnn_R_50_FPN_noaug_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Detectron1-Comparisons\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\LVISv0.5-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\LVISv0.5-InstanceSegmentation\\mask_rcnn_R_101_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\LVISv0.5-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\LVISv0.5-InstanceSegmentation\\mask_rcnn_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\LVISv0.5-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\LVISv0.5-InstanceSegmentation\\mask_rcnn_X_101_32x8d_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\LVISv0.5-InstanceSegmentation\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\LVISv1-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\LVISv1-InstanceSegmentation\\mask_rcnn_R_101_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\LVISv1-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\LVISv1-InstanceSegmentation\\mask_rcnn_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\LVISv1-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\LVISv1-InstanceSegmentation\\mask_rcnn_X_101_32x8d_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\LVISv1-InstanceSegmentation\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\cascade_mask_rcnn_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\cascade_mask_rcnn_R_50_FPN_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\mask_rcnn_R_50_FPN_1x_cls_agnostic.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\mask_rcnn_R_50_FPN_1x_dconv_c3-c5.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\mask_rcnn_R_50_FPN_3x_dconv_c3-c5.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\mask_rcnn_R_50_FPN_3x_gn.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\mask_rcnn_R_50_FPN_3x_syncbn.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\panoptic_fpn_R_101_dconv_cascade_gn_3x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\scratch_mask_rcnn_R_50_FPN_3x_gn.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\scratch_mask_rcnn_R_50_FPN_9x_gn.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\scratch_mask_rcnn_R_50_FPN_9x_syncbn.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\semantic_R_50_FPN_1x.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\PascalVOC-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\PascalVOC-Detection\\faster_rcnn_R_50_C4.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\PascalVOC-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\PascalVOC-Detection\\faster_rcnn_R_50_FPN.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\PascalVOC-Detection\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\cascade_mask_rcnn_R_50_FPN_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\cascade_mask_rcnn_R_50_FPN_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\fast_rcnn_R_50_FPN_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\fast_rcnn_R_50_FPN_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\keypoint_rcnn_R_50_FPN_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\keypoint_rcnn_R_50_FPN_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\keypoint_rcnn_R_50_FPN_normalized_training_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\keypoint_rcnn_R_50_FPN_training_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\mask_rcnn_R_50_C4_GCV_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\mask_rcnn_R_50_C4_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\mask_rcnn_R_50_C4_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\mask_rcnn_R_50_C4_training_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\mask_rcnn_R_50_DC5_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\mask_rcnn_R_50_FPN_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\mask_rcnn_R_50_FPN_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\mask_rcnn_R_50_FPN_pred_boxes_training_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\mask_rcnn_R_50_FPN_training_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\panoptic_fpn_R_50_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\panoptic_fpn_R_50_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\panoptic_fpn_R_50_training_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\retinanet_R_50_FPN_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\retinanet_R_50_FPN_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\rpn_R_50_FPN_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\rpn_R_50_FPN_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\semantic_R_50_FPN_inference_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\semantic_R_50_FPN_instant_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\quick_schedules\\semantic_R_50_FPN_training_acc_test.yaml -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\quick_schedules\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\fcos_R_50_FPN_1x.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Detection\\retinanet_R_50_FPN_1x.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Detection\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_regnetx_4gf_dds_fpn_1x.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_regnety_4gf_dds_fpn_1x.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_50_C4_1x.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\\mask_rcnn_R_50_FPN_1x.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-InstanceSegmentation\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-Keypoints\\keypoint_rcnn_R_50_FPN_1x.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-Keypoints\n",
            "      copying detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\\panoptic_fpn_R_50_1x.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\COCO-PanopticSegmentation\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\n",
            "      copying detectron2\\model_zoo\\configs\\common\\coco_schedule.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\n",
            "      copying detectron2\\model_zoo\\configs\\common\\optim.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\n",
            "      copying detectron2\\model_zoo\\configs\\common\\train.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\data\n",
            "      copying detectron2\\model_zoo\\configs\\common\\data\\coco.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\data\n",
            "      copying detectron2\\model_zoo\\configs\\common\\data\\coco_keypoint.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\data\n",
            "      copying detectron2\\model_zoo\\configs\\common\\data\\coco_panoptic_separated.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\data\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\models\n",
            "      copying detectron2\\model_zoo\\configs\\common\\models\\cascade_rcnn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\models\n",
            "      copying detectron2\\model_zoo\\configs\\common\\models\\fcos.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\models\n",
            "      copying detectron2\\model_zoo\\configs\\common\\models\\keypoint_rcnn_fpn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\models\n",
            "      copying detectron2\\model_zoo\\configs\\common\\models\\mask_rcnn_c4.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\models\n",
            "      copying detectron2\\model_zoo\\configs\\common\\models\\mask_rcnn_fpn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\models\n",
            "      copying detectron2\\model_zoo\\configs\\common\\models\\panoptic_fpn.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\models\n",
            "      copying detectron2\\model_zoo\\configs\\common\\models\\retinanet.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\common\\models\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\mmdet_mask_rcnn_R_50_FPN_1x.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      copying detectron2\\model_zoo\\configs\\Misc\\torchvision_imagenet_R_50.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\Misc\n",
            "      creating build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_regnetx_4gf_dds_FPN_100ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_regnetx_4gf_dds_FPN_200ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_regnetx_4gf_dds_FPN_400ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_regnety_4gf_dds_FPN_100ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_regnety_4gf_dds_FPN_200ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_regnety_4gf_dds_FPN_400ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_R_101_FPN_100ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_R_101_FPN_200ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_R_101_FPN_400ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_R_50_FPN_100ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_R_50_FPN_200ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_R_50_FPN_400ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      copying detectron2\\model_zoo\\configs\\new_baselines\\mask_rcnn_R_50_FPN_50ep_LSJ.py -> build\\lib.win-amd64-cpython-311\\detectron2\\model_zoo\\configs\\new_baselines\n",
            "      running build_ext\n",
            "      c:\\Users\\pruth\\anaconda3\\Lib\\site-packages\\torch\\utils\\cpp_extension.py:383: UserWarning: Error checking compiler version for cl: [WinError 2] The system cannot find the file specified\n",
            "        warnings.warn(f'Error checking compiler version for {compiler}: {error}')\n",
            "      building 'detectron2._C' extension\n",
            "      error: Microsoft Visual C++ 14.0 or greater is required. Get it with \"Microsoft C++ Build Tools\": https://visualstudio.microsoft.com/visual-cpp-build-tools/\n",
            "      [end of output]\n",
            "  \n",
            "  note: This error originates from a subprocess, and is likely not a problem with pip.\n",
            "  ERROR: Failed building wheel for detectron2\n",
            "ERROR: Could not build wheels for detectron2, which is required to install pyproject.toml-based projects\n"
          ]
        }
      ],
      "source": [
        "%pip install unstructured -q\n",
        "%pip install unstructured[local-inference] -q\n",
        "%pip install detectron2@git+https://github.com/facebookresearch/detectron2.git@v0.6#egg=detectron2 -q"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JUAsOqSK-f1v",
        "outputId": "a812578f-4e2d-4864-e759-7c5c617e8202"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: poppler-utils in c:\\users\\pruth\\anaconda3\\lib\\site-packages (0.1.0)\n",
            "Requirement already satisfied: Click>=7.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from poppler-utils) (8.1.7)\n",
            "Requirement already satisfied: colorama in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from Click>=7.0->poppler-utils) (0.4.6)\n",
            "Note: you may need to restart the kernel to use updated packages.\n"
          ]
        }
      ],
      "source": [
        "%pip install poppler-utils"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "DsPNYcU4Dh1C"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "15\n"
          ]
        }
      ],
      "source": [
        "from langchain.document_loaders import DirectoryLoader\n",
        "\n",
        "directory = 'C:\\\\Users\\\\pruth\\\\Downloads\\\\llm\\\\data'\n",
        "\n",
        "def load_docs(directory_path):\n",
        "    loader = DirectoryLoader(directory_path)\n",
        "    documents = loader.load()\n",
        "    return documents\n",
        "\n",
        "documents = load_docs(directory)\n",
        "print(len(documents))\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "S3EpWk7rDmw1"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "7588\n"
          ]
        }
      ],
      "source": [
        "from langchain.text_splitter import RecursiveCharacterTextSplitter\n",
        "\n",
        "def split_docs(documents,chunk_size=500,chunk_overlap=20):\n",
        "  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)\n",
        "  docs = text_splitter.split_documents(documents)\n",
        "  return docs\n",
        "\n",
        "docs = split_docs(documents)\n",
        "print(len(docs))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "3.2 Trust is vital to the ability of our country to achieve sustained growth in mining sector. State will endeavor continuously to increase trust level between government, miners, local communities and other stakeholders through openness, fairness, better regulation, responsiveness, inclusive policy making.\n",
            "\n",
            "4. PROSPECTING AND EXPLORATION\n"
          ]
        }
      ],
      "source": [
        "print(docs[18].page_content)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Note: you may need to restart the kernel to use updated packages.\n"
          ]
        }
      ],
      "source": [
        "%pip install tiktoken -q"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {},
      "outputs": [],
      "source": [
        "from langchain.embeddings import SentenceTransformerEmbeddings\n",
        "embeddings = SentenceTransformerEmbeddings(model_name=\"all-MiniLM-L6-v2\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "384"
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "query_result = embeddings.embed_query(\"Hello world\")\n",
        "len(query_result)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: pinecone-client in c:\\users\\pruth\\anaconda3\\lib\\site-packages (2.2.4)Note: you may need to restart the kernel to use updated packages.\n",
            "\n",
            "Requirement already satisfied: requests>=2.19.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pinecone-client) (2.31.0)\n",
            "Requirement already satisfied: pyyaml>=5.4 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pinecone-client) (6.0)\n",
            "Requirement already satisfied: loguru>=0.5.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pinecone-client) (0.7.2)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pinecone-client) (4.7.1)\n",
            "Requirement already satisfied: dnspython>=2.0.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pinecone-client) (2.4.2)\n",
            "Requirement already satisfied: python-dateutil>=2.5.3 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pinecone-client) (2.8.2)\n",
            "Requirement already satisfied: urllib3>=1.21.1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pinecone-client) (1.26.16)\n",
            "Requirement already satisfied: tqdm>=4.64.1 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pinecone-client) (4.65.0)\n",
            "Requirement already satisfied: numpy>=1.22.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from pinecone-client) (1.24.3)\n",
            "Requirement already satisfied: colorama>=0.3.4 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from loguru>=0.5.0->pinecone-client) (0.4.6)\n",
            "Requirement already satisfied: win32-setctime>=1.0.0 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from loguru>=0.5.0->pinecone-client) (1.1.0)\n",
            "Requirement already satisfied: six>=1.5 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from python-dateutil>=2.5.3->pinecone-client) (1.16.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests>=2.19.0->pinecone-client) (2.0.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests>=2.19.0->pinecone-client) (3.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\pruth\\anaconda3\\lib\\site-packages (from requests>=2.19.0->pinecone-client) (2023.7.22)\n"
          ]
        }
      ],
      "source": [
        "%pip install pinecone-client "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {},
      "outputs": [],
      "source": [
        "import pinecone \n",
        "from langchain.vectorstores import Pinecone\n",
        "\n",
        "pinecone.init(\n",
        "    api_key=\"de3defb8-3e52-4ccf-82b1-9d785b981ec5\",  # find at app.pinecone.io\n",
        "    environment=\"gcp-starter\"  # next to api key in console\n",
        ")\n",
        "\n",
        "index_name = \"langchain-chatbot\"\n",
        "\n",
        "index = Pinecone.from_documents(docs, embeddings, index_name=index_name)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[(Document(page_content='THE MINES ACT, 1952 (Act No. 35 of 1952 ) (15 March, 1952) (As modified upto 1983)\\n\\nAn Act to amend and consolidate the law relating to the Regulation of labour and safety in mines\\n\\nBe it enacted by Parliament as follows :-\\n\\nCHAPTER I PRELIMINARY\\n\\n1.\\n\\n2.', metadata={'source': 'C:\\\\Users\\\\pruth\\\\Downloads\\\\llm\\\\data\\\\theminesact1952.pdf'}),\n",
              "  0.801203728)]"
            ]
          },
          "execution_count": 14,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "def get_similiar_docs(query,k=1,score=True):\n",
        "  if score:\n",
        "    similar_docs = index.similarity_search_with_score(query,k=k)\n",
        "  else:\n",
        "    similar_docs = index.similarity_search(query,k=k)\n",
        "  return similar_docs\n",
        "\n",
        "query = \"Can you explain the key provisions of the Mines Act\"\n",
        "similar_docs = get_similiar_docs(query)\n",
        "similar_docs"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.11.4"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
