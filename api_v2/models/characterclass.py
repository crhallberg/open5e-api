"""The model for a feat."""
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .abstracts import HasName, HasDescription, Modification
from .document import FromDocument

class FeatureItem(models.Model):
    """This is the class for an individual class feature item, a subset of a class
    feature. The name field is unused."""
    # Somewhere in here is where you'd define a field that would eventually display as "Rage Damage +2"

    feature = models.ForeignKey('Feature', on_delete=models.CASCADE)
    level = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(20)])

    def __str__(self):
        return "{} {} ({})".format(
                                 self.feature.character_class.name,
                                 str(self.level),
                                 self.feature.name)

class Feature(HasName, HasDescription, FromDocument):
    """This class represents an individual class feature, such as Rage, or Extra
    Attack."""

    character_class = models.ForeignKey('CharacterClass',
        on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.name,self.character_class.name)


class CharacterClass(HasName, FromDocument):
    """The model for a character class or subclass."""
    subclass_of = models.ForeignKey('self',
                                   default=None,
                                   blank=True,
                                   null=True,
                                   on_delete=models.CASCADE)
    
    @property
    def is_subclass(self):
        """Returns whether the object is a subclass."""
        return self.subclass_of is not None

    @property
    def features(self):
        """Returns the set of features that are related to this class."""
        return self.feature_set

    def levels(self):
        by_level = {}

        for feature in self.feature_set.all():
            for fl in feature.featureitem_set.all():
                if (str(fl.level)) not in by_level.keys():
                    by_level[str(fl.level)] = {}
                    by_level[str(fl.level)]['features'] = []
                
                by_level[str(fl.level)]['features'].append(fl.feature.key)
                by_level[str(fl.level)]['proficiency-bonus'] = self.proficiency_bonus(player_level=fl.level)
                
        return by_level

    def proficiency_bonus(self, player_level):
        # Consider as part of enums
        p = [0,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]
        return p[player_level]