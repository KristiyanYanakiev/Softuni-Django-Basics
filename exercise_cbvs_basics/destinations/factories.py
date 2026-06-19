import factory
from factory.django import DjangoModelFactory
from .models import Destination


class DestinationFactory(DjangoModelFactory):
    class Meta:
        model = Destination
        # Optional: if you want to prevent database integrity errors during massive seeding,
        # you can tell factory_boy to check for existing records first:
        # django_get_or_create = ('name', 'country')

    # 1. Sequence guarantees uniqueness to satisfy your unique_together constraint
    name = factory.Sequence(lambda n: f"Adventure Resort {n}")

    # 2. Randomly select valid 2-letter country codes matching your choices
    country = factory.Faker('country_code', representation='alpha-2')

    # 3. Random valid price matching max_digits=6 and decimal_places=2 (e.g., 100.00 to 999.99)
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)

    description = factory.Faker('paragraph', nb_sentences=4)
    duration_days = factory.Faker('random_int', min=1, max=14)
    is_available = True

    # Note on Slug: We don't define a slug factory field here because your
    # model's custom .save() method automatically handles slugify(self.name)!

    # 4. Handle ManyToMany relationships gracefully if needed
    @factory.post_generation
    def travelers(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do not add relations
            return

        if extracted:
            # If an explicit list of travelers is passed, add them
            for traveler in extracted:
                self.travelers.add(traveler)