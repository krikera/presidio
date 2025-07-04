"""Predefined recognizers package. Holds all the default recognizers."""

# NER recognizers
from presidio_analyzer.predefined_recognizers.ner.transformers_recognizer import (
    TransformersRecognizer,
)
from .ner.azure_ai_language import AzureAILanguageRecognizer
from .ner.gliner_recognizer import GLiNERRecognizer
from .ner.spacy_recognizer import SpacyRecognizer
from .ner.stanza_recognizer import StanzaRecognizer

# US recognizers
from .country_specific.us.aba_routing_recognizer import AbaRoutingRecognizer
from .country_specific.us.us_bank_recognizer import UsBankRecognizer
from .country_specific.us.us_driver_license_recognizer import UsLicenseRecognizer
from .country_specific.us.us_itin_recognizer import UsItinRecognizer
from .country_specific.us.us_passport_recognizer import UsPassportRecognizer
from .country_specific.us.us_ssn_recognizer import UsSsnRecognizer

# UK recognizers
from .country_specific.uk.uk_nhs_recognizer import NhsRecognizer
from .country_specific.uk.uk_nino_recognizer import UkNinoRecognizer

# India recognizers
from .country_specific.india.in_aadhaar_recognizer import InAadhaarRecognizer
from .country_specific.india.in_pan_recognizer import InPanRecognizer
from .country_specific.india.in_passport_recognizer import InPassportRecognizer
from .country_specific.india.in_vehicle_registration_recognizer import InVehicleRegistrationRecognizer
from .country_specific.india.in_voter_recognizer import InVoterRecognizer

# Italy recognizers
from .country_specific.italy.it_driver_license_recognizer import ItDriverLicenseRecognizer
from .country_specific.italy.it_fiscal_code_recognizer import ItFiscalCodeRecognizer
from .country_specific.italy.it_identity_card_recognizer import ItIdentityCardRecognizer
from .country_specific.italy.it_passport_recognizer import ItPassportRecognizer
from .country_specific.italy.it_vat_code import ItVatCodeRecognizer

# Australia recognizers
from .country_specific.australia.au_abn_recognizer import AuAbnRecognizer
from .country_specific.australia.au_acn_recognizer import AuAcnRecognizer
from .country_specific.australia.au_medicare_recognizer import AuMedicareRecognizer
from .country_specific.australia.au_tfn_recognizer import AuTfnRecognizer

# Spain recognizers
from .country_specific.spain.es_nie_recognizer import EsNieRecognizer
from .country_specific.spain.es_nif_recognizer import EsNifRecognizer

# Finland recognizers
from .country_specific.finland.fi_personal_identity_code_recognizer import FiPersonalIdentityCodeRecognizer

# Poland recognizers
from .country_specific.poland.pl_pesel_recognizer import PlPeselRecognizer

# Singapore recognizers
from .country_specific.singapore.sg_fin_recognizer import SgFinRecognizer
from .country_specific.singapore.sg_uen_recognizer import SgUenRecognizer

# Generic recognizers
from .generic.credit_card_recognizer import CreditCardRecognizer
from .generic.crypto_recognizer import CryptoRecognizer
from .generic.date_recognizer import DateRecognizer
from .generic.email_recognizer import EmailRecognizer
from .generic.iban_recognizer import IbanRecognizer
from .generic.ip_recognizer import IpRecognizer
from .generic.medical_license_recognizer import MedicalLicenseRecognizer
from .generic.phone_recognizer import PhoneRecognizer
from .generic.url_recognizer import UrlRecognizer

PREDEFINED_RECOGNIZERS = [
    "PhoneRecognizer",
    "CreditCardRecognizer",
    "CryptoRecognizer",
    "DateRecognizer",
    "EmailRecognizer",
    "IpRecognizer",
    "IbanRecognizer",
    "MedicalLicenseRecognizer",
    "UrlRecognizer",
]

NLP_RECOGNIZERS = {
    "spacy": SpacyRecognizer,
    "stanza": StanzaRecognizer,
    "transformers": TransformersRecognizer,
}

__all__ = [
    "AbaRoutingRecognizer",
    "CreditCardRecognizer",
    "CryptoRecognizer",
    "DateRecognizer",
    "EmailRecognizer",
    "IbanRecognizer",
    "IpRecognizer",
    "NhsRecognizer",
    "MedicalLicenseRecognizer",
    "PhoneRecognizer",
    "SgFinRecognizer",
    "UrlRecognizer",
    "UsBankRecognizer",
    "UsItinRecognizer",
    "UsLicenseRecognizer",
    "UsPassportRecognizer",
    "UsSsnRecognizer",
    "EsNifRecognizer",
    "SpacyRecognizer",
    "StanzaRecognizer",
    "NLP_RECOGNIZERS",
    "AuAbnRecognizer",
    "AuAcnRecognizer",
    "AuTfnRecognizer",
    "AuMedicareRecognizer",
    "TransformersRecognizer",
    "ItDriverLicenseRecognizer",
    "ItFiscalCodeRecognizer",
    "ItVatCodeRecognizer",
    "ItIdentityCardRecognizer",
    "ItPassportRecognizer",
    "InPanRecognizer",
    "GLiNERRecognizer",
    "PlPeselRecognizer",
    "AzureAILanguageRecognizer",
    "InAadhaarRecognizer",
    "InVehicleRegistrationRecognizer",
    "SgUenRecognizer",
    "InVoterRecognizer",
    "InPassportRecognizer",
    "FiPersonalIdentityCodeRecognizer",
    "EsNieRecognizer",
    "UkNinoRecognizer",
]
