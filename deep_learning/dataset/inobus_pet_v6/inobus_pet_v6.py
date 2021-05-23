"""inobus_pet_v6 dataset."""
import itertools
from pathlib import Path

import tensorflow_datasets as tfds

# TODO(inobus_pet_v6): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Shape: (2464, 3280, 3). (H, W, C) format.
inobus_pet_v5에, Sharpen, Gaussian Blur, Box Blur, Contrast Brighten augmentation 추가.
Testset은 Augmentation 없이 동일하다.

- train
    - yes_pet: 647 * 6 = 3882장
    - no_pet:  95 * 6 = 570장
- test
    - yes_pet: 100장
    - no_pet:  40장
"""

# TODO(inobus_pet_v6): BibTeX citation
_CITATION = """
"""

_PATH = "/Users/minhoheo/Downloads/inobus_pet_v6"


class InobusPetV6(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for inobus_pet_v6 dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(2464, 3280, 3)),
            'label': tfds.features.ClassLabel(names=['no_pet', 'yes_pet']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'label'),  # Set to `None` to disable
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = Path(_PATH)

    return {
        'train': self._generate_examples(path / 'train'),
        'test': self._generate_examples(path / 'test')
    }

  def _generate_examples(self, path):
    """Yields examples."""
    # Yields (key, example) tuples from the dataset
    paths = itertools.chain((path.rglob('*.jpeg')), path.rglob('*.jpg'),
                            path.rglob('*.JPG'))
    for image_path in paths:
      key = image_path.parent.name + '/' + image_path.name
      yield key, {
          'image': image_path,
          'label': image_path.parent.name,
      }
