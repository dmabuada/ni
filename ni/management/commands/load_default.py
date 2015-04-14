from __future__ import print_function
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = "Load basic data for ni."

    def handle_noargs(self, **options):
        from sample_dress_data_loader import load_sample_data, category_url

        from satchmo_store.contact.models import (
            AddressBook,
            Contact,
            ContactOrganization,
            ContactOrganizationRole,
            ContactInteractionType,
            ContactRole,
            Organization,
            PhoneNumber,
        )
        from product.models import (
            Category,
            OptionGroup,
            Option,
            Price,
            Product,
            ProductImage
        )
        from product.modules.configurable.models import ConfigurableProduct

        from satchmo_store.shop.models import Config
        from django.conf import settings
        from l10n.models import Country
        from django.contrib.sites.models import Site
        from django.contrib.auth.models import User
        from django.utils.text import slugify
        from django.core.files import File  # TODO: save files
        from django.core.files.base import ContentFile
        from django.core.files.temp import NamedTemporaryFile
        # idempotency test

        print("Checking for existing sample data.")
        try:
            p = Product.objects.get(slug="dresses")
            print("It looks like you already loaded the sample store data.")
            import sys

            sys.exit(1)
        except Product.DoesNotExist:
            pass

        print("Loading sample store data.")

        # Load basic configuration information

        print("Creating site...")

        try:
            site = Site.objects.get(id=settings.SITE_ID)
            print("Using existing site #{}".format(settings.SITE_ID))
        except Site.DoesNotExist:
            print("Creating Example Store Site")
            site = Site(domain="localhost", name="Sample Store")

        site.domain = settings.SITE_DOMAIN
        site.name = settings.SITE_NAME
        site.save()
        try:
            store_country = Country.objects.get(iso3_code='USA')
        except Country.DoesNotExist:
            print(
                "\nError: Country data should be first loaded by:  "
                "python manage.py satchmo_load_l10n"
            )
            import sys

            sys.exit(1)
        config = Config(site=site, store_name=settings.SITE_NAME,
                        country=store_country, sales_country=store_country)
        config.save()
        config.shipping_countries.add(store_country)
        config.save()
        print("Creating Customers...")
        # Import some customers

        customer = ContactRole(name='Customer')
        supplier = ContactRole(name="Supplier")
        distributor = ContactRole(name="Distributor")

        customer.save()
        supplier.save()
        distributor.save()

        company = ContactOrganization(name="Company")
        government = ContactOrganization(name="Government")
        nonprofit = ContactOrganization(name="Non-profit")

        company.save()
        government.save()
        nonprofit.save()

        supplier_org_role = ContactOrganizationRole(name='Supplier')
        distributor_org_role = ContactOrganizationRole(name='Distributor')
        manufacturer_org_role = ContactOrganizationRole(name='Manufacturer')
        customer_org_role = ContactOrganizationRole(name='Customer')

        supplier_org_role.save()
        distributor_org_role .save()
        manufacturer_org_role.save()
        customer_org_role.save()

        email_interaction = ContactInteractionType(name='Email')
        phone_interaction = ContactInteractionType(name='Phone')
        in_person_interaction = ContactInteractionType(name='In Person')

        email_interaction.save()
        phone_interaction.save()
        in_person_interaction.save()


        c1 = Contact(
            first_name="Chris",
            last_name="Smith",
            email="chris@aol.com",
            role=customer,
            notes="Really cool stuff")
        c1.save()

        p1 = PhoneNumber(
            contact=c1,
            phone="601-555-5511",
            type="Home",
            primary=True
        )
        p1.save()

        c2 = Contact(
            first_name="John",
            last_name="Smith",
            email="abc@comcast.com",
            role=customer,
            notes="Second user"
        )
        c2.save()

        p2 = PhoneNumber(
            contact=c2,
            phone="999-555-5111",
            type="Work",
            primary=True
        )
        p2.save()

        # Import some addresses for these customers
        us = Country.objects.get(iso2_code='US')
        a1 = AddressBook(
            description="Home",
            street1="8235 Pike Street",
            city="Anywhere Town",
            state="TN",
            postal_code="38138",
            country=us,
            is_default_shipping=True,
            contact=c1
        )
        a1.save()

        a2 = AddressBook(
            description="Work",
            street1="1245 Main Street",
            city="Stillwater",
            state="MN",
            postal_code="55082",
            country=us,
            is_default_shipping=True,
            contact=c2
        )
        a2.save()

        print("Creating Suppliers...")
        # Import some suppliers

        # supplier = ContactOrganizationRole.objects.get(pk='Supplier')
        # company = ContactOrganization.objects.get(pk='Company')
        # contactsupplier = ContactRole.objects.get(pk='Supplier')
        org1 = Organization(
            name="Rhinestone Ronny",
            type=company,
            role=supplier_org_role
        )
        org1.save()
        c4 = Contact(
            first_name="Fred",
            last_name="Jones",
            email="fj@rr.com",
            role=supplier,
            organization=org1
        )
        c4.save()
        p4 = PhoneNumber(contact=c4, phone="800-188-7611", type="Work",
                         primary=True)
        p4.save()
        p5 = PhoneNumber(contact=c4, phone="755-555-1111", type="Fax")
        p5.save()
        a3 = AddressBook(
            contact=c4,
            description="Mailing address",
            street1="Receiving Dept",
            street2="918 Funky Town St",
            city="Fishkill",
            state="NJ", country=us,
            postal_code="19010"
        )
        a3.save()

        print("Creating Categories...")

        dresses_category = Category(
            site=site,
            name="Dresses",
            slug="dresses",
            description="Dresses for all"
        )
        dresses_category.save()

        formal_dresses_category = Category(
            site=site,
            name="Formal Dresses",
            slug="formal",
            description="Formal dresses",
            parent=dresses_category
        )
        cocktail_dresses_category = Category(
            site=site,
            name="Cocktail Dresses",
            slug="cocktail",
            description="Cocktail dresses",
            parent=dresses_category
        )
        night_out_dresses_category = Category(
            site=site,
            name="Night-out Dresses",
            slug="night-out",
            description="Night-out dresses",
            parent=dresses_category
        )
        party_dresses_category = Category(
            site=site,
            name="Party dresses",
            slug="party",
            description="Party dresses",
            parent=dresses_category
        )

        formal_dresses_category.save()
        cocktail_dresses_category.save()
        night_out_dresses_category.save()
        party_dresses_category.save()

        print("Creating Products...")

        def populate_category(src_category_name, category):
            sample_data = load_sample_data(src_category_name)
            for i, datum in enumerate(sample_data):
                # Create dress itself
                this_dress = Product(
                    site=site,
                    name=datum['name'],
                    slug=slugify(datum['name']),
                    description=datum['description'],
                    featured=i < 2
                )
                this_dress.save()

                # Create price
                price = Price(price=datum['price'], product=this_dress)
                price.save()

                # Add to appropriate category
                this_dress.category.add(category)
                this_dress.save()

                dress_image = ProductImage(
                    product=this_dress,
                    picture=ContentFile(
                        datum['image-stream'].read(),
                        name=slugify(datum['name'])
                    )
                )
                dress_image.save()

                # Create variations
                size_option_group = OptionGroup(
                    site=site,
                    name="size",
                    sort_order=1
                )
                size_option_group.save()

                for j, size in enumerate([str(n) for n in range(0, 18, 2)]):
                    variation = Option(
                        name=size,
                        value=size,
                        sort_order=j,
                        option_group=size_option_group
                    )
                    variation.save()

                dress_variation = ConfigurableProduct(product=this_dress)
                dress_variation.save()
                dress_variation.option_group.add(size_option_group)
                dress_variation.save()
                dress_variation.create_all_variations()

        print('    - black tie')
        populate_category(category_url('black_tie'), formal_dresses_category)

        print('    - cocktail')
        populate_category(category_url('cocktail'), cocktail_dresses_category)

        print('    - night out')
        populate_category(category_url('night_out'), night_out_dresses_category)

        print('    - party')
        populate_category(category_url('daytime'), party_dresses_category)

        print("Create a test user...")
        # First see if our test user is still there, then use or create that user
        try:
            test_user = User.objects.get(username="csmith")
        except:
            test_user = User.objects.create_user('csmith',
                                                 'tester@testsite.com', 'test')
            test_user.save()
        c1.user = test_user
        c1.save()

