"""
 Copyright (c) 2022, salesforce.com, inc.
 All rights reserved.
 SPDX-License-Identifier: BSD-3-Clause
 For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
"""

import os
from pefomed.common.registry import registry

from pefomed.datasets.builders.base_dataset_builder import BaseDatasetBuilder
from pefomed.datasets.datasets.image_text_pair_datasets import ImageTextPairDataset, ImageTextPairInstructDataset
# from pefomed.datasets.datasets.general.laion_dataset import LaionDataset, LaionInstructDataset
from pefomed.datasets.datasets.medical.mscxr_dataset import MSCXRDataset, MSCXREvalDataset

@registry.register_builder("mscxr")
class MSCXRBuilder(BaseDatasetBuilder):
    train_dataset_cls = MSCXRDataset
    eval_dataset_cls = MSCXREvalDataset
    DATASET_CONFIG_DICT = {
        "default": "configs/datasets/medical/mscxr/defaults.yaml",
    }

@registry.register_builder("conceptual_caption_3m")
class ConceptualCaption3MBuilder(BaseDatasetBuilder):
    train_dataset_cls = ImageTextPairDataset

    DATASET_CONFIG_DICT = {
        "default": "configs/datasets/conceptual_caption/defaults_3m.yaml"
    }

@registry.register_builder("conceptual_caption_3m_instruct")
class ConceptualCaption3MInstructBuilder(BaseDatasetBuilder):
    train_dataset_cls = ImageTextPairInstructDataset

    DATASET_CONFIG_DICT = {
        "default": "configs/datasets/conceptual_caption/defaults_3m_instruct.yaml"
    }


@registry.register_builder("conceptual_caption_12m")
class ConceptualCaption12MBuilder(BaseDatasetBuilder):
    train_dataset_cls = ImageTextPairDataset

    DATASET_CONFIG_DICT = {
        "default": "configs/datasets/conceptual_caption/defaults_12m.yaml"
    }

@registry.register_builder("conceptual_caption_12m_instruct")
class ConceptualCaption12MInstructBuilder(BaseDatasetBuilder):
    train_dataset_cls = ImageTextPairInstructDataset

    DATASET_CONFIG_DICT = {
        "default": "configs/datasets/conceptual_caption/defaults_12m_instruct.yaml"
    }

@registry.register_builder("sbu_caption")
class SBUCaptionBuilder(BaseDatasetBuilder):
    train_dataset_cls = ImageTextPairDataset

    DATASET_CONFIG_DICT = {"default": "configs/datasets/sbu_caption/defaults.yaml"}


@registry.register_builder("sbu_caption_instruct")
class SBUCaptionInstructBuilder(BaseDatasetBuilder):
    train_dataset_cls = ImageTextPairInstructDataset

    DATASET_CONFIG_DICT = {"default": "configs/datasets/sbu_caption/defaults_instruct.yaml"}


@registry.register_builder("vg_caption")
class VGCaptionBuilder(BaseDatasetBuilder):
    train_dataset_cls = ImageTextPairDataset

    DATASET_CONFIG_DICT = {"default": "configs/datasets/vg/defaults_caption.yaml"}


@registry.register_builder("vg_caption_instruct")
class VGCaptionInstructBuilder(BaseDatasetBuilder):
    train_dataset_cls = ImageTextPairInstructDataset

    DATASET_CONFIG_DICT = {"default": "configs/datasets/vg/defaults_caption_instruct.yaml"}



# @registry.register_builder("laion2B_multi")
# class Laion2BMultiBuilder(BaseDatasetBuilder):
#     train_dataset_cls = LaionDataset

#     DATASET_CONFIG_DICT = {"default": "configs/datasets/laion/defaults_2B_multi.yaml"}

#     def _download_ann(self):
#         pass

#     def _download_vis(self):
#         pass

#     def build(self):
#         self.build_processors()

#         build_info = self.config.build_info

#         datasets = dict()
#         split = "train"  # laion dataset only has train split

#         # create datasets
#         # [NOTE] return inner_datasets (wds.DataPipeline)
#         dataset_cls = self.train_dataset_cls
#         datasets[split] = dataset_cls(
#             vis_processor=self.vis_processors[split],
#             text_processor=self.text_processors[split],
#             location=build_info.storage,
#         ).inner_dataset

#         return datasets

# @registry.register_builder("laion400M")
# class Laion400MBuilder(Laion2BMultiBuilder):
#     train_dataset_cls = LaionDataset

#     DATASET_CONFIG_DICT = {"default": "configs/datasets/laion/defaults_400M.yaml"}


# @registry.register_builder("laion400M_instruct")
# class Laion400MInstructBuilder(Laion2BMultiBuilder):
#     train_dataset_cls = LaionInstructDataset

#     DATASET_CONFIG_DICT = {"default": "configs/datasets/laion/defaults_400M_instruct.yaml"}

