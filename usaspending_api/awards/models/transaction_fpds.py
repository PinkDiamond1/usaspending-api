from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class TransactionFPDS(models.Model):
    transaction = models.OneToOneField(
        "awards.TransactionNormalized",
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="contract_data",
        help_text="Non-specific transaction data, fields shared among both assistance and contract transactions",
    )
    detached_award_procurement_id = models.IntegerField(blank=True, null=True, db_index=True)
    detached_award_proc_unique = models.TextField(unique=True, null=True)
    piid = models.TextField(blank=True, null=True, db_index=True)
    agency_id = models.TextField(blank=True, null=True)
    awarding_sub_tier_agency_c = models.TextField(blank=True, null=True)
    awarding_sub_tier_agency_n = models.TextField(blank=True, null=True)
    awarding_agency_code = models.TextField(blank=True, null=True)
    awarding_agency_name = models.TextField(blank=True, null=True)
    parent_award_id = models.TextField(blank=True, null=True, db_index=True)
    award_modification_amendme = models.TextField(blank=True, null=True)
    type_of_contract_pricing = models.TextField(blank=True, null=True, db_index=True)
    type_of_contract_pric_desc = models.TextField(blank=True, null=True)
    contract_award_type = models.TextField(blank=True, null=True)
    contract_award_type_desc = models.TextField(blank=True, null=True)
    naics = models.TextField(blank=True, null=True, db_index=True)
    naics_description = models.TextField(blank=True, null=True)
    awardee_or_recipient_uei = models.TextField(blank=True, null=True)
    awardee_or_recipient_uei_n = models.TextField(blank=True, null=True)
    awardee_or_recipient_uniqu = models.TextField(blank=True, null=True)
    ultimate_parent_legal_enti = models.TextField(blank=True, null=True)
    ultimate_parent_uei = models.TextField(blank=True, null=True)
    ultimate_parent_uei_name = models.TextField(blank=True, null=True)
    ultimate_parent_unique_ide = models.TextField(blank=True, null=True)
    award_description = models.TextField(blank=True, null=True)
    place_of_performance_zip4a = models.TextField(blank=True, null=True)
    place_of_performance_zip5 = models.TextField(blank=True, null=True)
    place_of_perform_zip_last4 = models.TextField(blank=True, null=True)
    place_of_perform_city_name = models.TextField(blank=True, null=True)
    place_of_perform_county_na = models.TextField(blank=True, null=True)
    place_of_perform_county_co = models.TextField(blank=True, null=True)
    place_of_performance_congr = models.TextField(blank=True, null=True)
    awardee_or_recipient_legal = models.TextField(blank=True, null=True)
    legal_entity_city_name = models.TextField(blank=True, null=True)
    legal_entity_state_code = models.TextField(blank=True, null=True)
    legal_entity_state_descrip = models.TextField(blank=True, null=True)
    legal_entity_county_code = models.TextField(blank=True, null=True)
    legal_entity_county_name = models.TextField(blank=True, null=True)
    legal_entity_zip4 = models.TextField(blank=True, null=True)
    legal_entity_zip5 = models.TextField(blank=True, null=True)
    legal_entity_zip_last4 = models.TextField(blank=True, null=True)
    legal_entity_congressional = models.TextField(blank=True, null=True)
    legal_entity_address_line1 = models.TextField(blank=True, null=True)
    legal_entity_address_line2 = models.TextField(blank=True, null=True)
    legal_entity_address_line3 = models.TextField(blank=True, null=True)
    legal_entity_country_code = models.TextField(blank=True, null=True)
    legal_entity_country_name = models.TextField(blank=True, null=True)
    period_of_performance_star = models.TextField(blank=True, null=True)
    period_of_performance_curr = models.TextField(blank=True, null=True)
    period_of_perf_potential_e = models.TextField(blank=True, null=True)
    ordering_period_end_date = models.TextField(blank=True, null=True)
    action_date = models.TextField(blank=True, null=True)
    action_type = models.TextField(blank=True, null=True)
    action_type_description = models.TextField(blank=True, null=True)
    federal_action_obligation = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    current_total_value_award = models.TextField(blank=True, null=True)
    potential_total_value_awar = models.TextField(blank=True, null=True)
    total_obligated_amount = models.TextField(blank=True, null=True)
    base_exercised_options_val = models.TextField(blank=True, null=True)
    base_and_all_options_value = models.TextField(blank=True, null=True)
    funding_sub_tier_agency_co = models.TextField(blank=True, null=True)
    funding_sub_tier_agency_na = models.TextField(blank=True, null=True)
    funding_office_code = models.TextField(blank=True, null=True)
    funding_office_name = models.TextField(blank=True, null=True)
    awarding_office_code = models.TextField(blank=True, null=True)
    awarding_office_name = models.TextField(blank=True, null=True)
    referenced_idv_agency_iden = models.TextField(blank=True, null=True)
    referenced_idv_agency_desc = models.TextField(blank=True, null=True)
    funding_agency_code = models.TextField(blank=True, null=True)
    funding_agency_name = models.TextField(blank=True, null=True)
    place_of_performance_locat = models.TextField(blank=True, null=True)
    place_of_performance_state = models.TextField(blank=True, null=True)
    place_of_perfor_state_desc = models.TextField(blank=True, null=True)
    place_of_perform_country_c = models.TextField(blank=True, null=True)
    place_of_perf_country_desc = models.TextField(blank=True, null=True)
    idv_type = models.TextField(blank=True, null=True)
    idv_type_description = models.TextField(blank=True, null=True)
    award_or_idv_flag = models.TextField(blank=True, null=True)
    referenced_idv_type = models.TextField(blank=True, null=True)
    referenced_idv_type_desc = models.TextField(blank=True, null=True)
    vendor_doing_as_business_n = models.TextField(blank=True, null=True)
    vendor_phone_number = models.TextField(blank=True, null=True)
    vendor_fax_number = models.TextField(blank=True, null=True)
    multiple_or_single_award_i = models.TextField(blank=True, null=True)
    multiple_or_single_aw_desc = models.TextField(blank=True, null=True)
    referenced_mult_or_single = models.TextField(blank=True, null=True)
    referenced_mult_or_si_desc = models.TextField(blank=True, null=True)
    type_of_idc = models.TextField(blank=True, null=True)
    type_of_idc_description = models.TextField(blank=True, null=True)
    a_76_fair_act_action = models.TextField(blank=True, null=True)
    a_76_fair_act_action_desc = models.TextField(blank=True, null=True)
    dod_claimant_program_code = models.TextField(blank=True, null=True)
    dod_claimant_prog_cod_desc = models.TextField(blank=True, null=True)
    clinger_cohen_act_planning = models.TextField(blank=True, null=True)
    clinger_cohen_act_pla_desc = models.TextField(blank=True, null=True)
    commercial_item_acquisitio = models.TextField(blank=True, null=True)
    commercial_item_acqui_desc = models.TextField(blank=True, null=True)
    commercial_item_test_progr = models.TextField(blank=True, null=True)
    commercial_item_test_desc = models.TextField(blank=True, null=True)
    consolidated_contract = models.TextField(blank=True, null=True)
    consolidated_contract_desc = models.TextField(blank=True, null=True)
    contingency_humanitarian_o = models.TextField(blank=True, null=True)
    contingency_humanitar_desc = models.TextField(blank=True, null=True)
    contract_bundling = models.TextField(blank=True, null=True)
    contract_bundling_descrip = models.TextField(blank=True, null=True)
    contract_financing = models.TextField(blank=True, null=True)
    contract_financing_descrip = models.TextField(blank=True, null=True)
    contracting_officers_deter = models.TextField(blank=True, null=True)
    contracting_officers_desc = models.TextField(blank=True, null=True)
    cost_accounting_standards = models.TextField(blank=True, null=True)
    cost_accounting_stand_desc = models.TextField(blank=True, null=True)
    cost_or_pricing_data = models.TextField(blank=True, null=True)
    cost_or_pricing_data_desc = models.TextField(blank=True, null=True)
    country_of_product_or_serv = models.TextField(blank=True, null=True)
    country_of_product_or_desc = models.TextField(blank=True, null=True)
    construction_wage_rate_req = models.TextField(blank=True, null=True)
    construction_wage_rat_desc = models.TextField(blank=True, null=True)
    evaluated_preference = models.TextField(blank=True, null=True)
    evaluated_preference_desc = models.TextField(blank=True, null=True)
    extent_competed = models.TextField(blank=True, null=True, db_index=True)
    extent_compete_description = models.TextField(blank=True, null=True)
    fed_biz_opps = models.TextField(blank=True, null=True)
    fed_biz_opps_description = models.TextField(blank=True, null=True)
    foreign_funding = models.TextField(blank=True, null=True)
    foreign_funding_desc = models.TextField(blank=True, null=True)
    government_furnished_prope = models.TextField(blank=True, null=True)
    government_furnished_desc = models.TextField(blank=True, null=True)
    information_technology_com = models.TextField(blank=True, null=True)
    information_technolog_desc = models.TextField(blank=True, null=True)
    interagency_contracting_au = models.TextField(blank=True, null=True)
    interagency_contract_desc = models.TextField(blank=True, null=True)
    local_area_set_aside = models.TextField(blank=True, null=True)
    local_area_set_aside_desc = models.TextField(blank=True, null=True)
    major_program = models.TextField(blank=True, null=True)
    purchase_card_as_payment_m = models.TextField(blank=True, null=True)
    purchase_card_as_paym_desc = models.TextField(blank=True, null=True)
    multi_year_contract = models.TextField(blank=True, null=True)
    multi_year_contract_desc = models.TextField(blank=True, null=True)
    national_interest_action = models.TextField(blank=True, null=True)
    national_interest_desc = models.TextField(blank=True, null=True)
    number_of_actions = models.TextField(blank=True, null=True)
    number_of_offers_received = models.TextField(blank=True, null=True)
    other_statutory_authority = models.TextField(blank=True, null=True)
    performance_based_service = models.TextField(blank=True, null=True)
    performance_based_se_desc = models.TextField(blank=True, null=True)
    place_of_manufacture = models.TextField(blank=True, null=True)
    place_of_manufacture_desc = models.TextField(blank=True, null=True)
    price_evaluation_adjustmen = models.TextField(blank=True, null=True)
    product_or_service_code = models.TextField(blank=True, null=True, db_index=True)
    product_or_service_co_desc = models.TextField(blank=True, null=True)
    program_acronym = models.TextField(blank=True, null=True)
    other_than_full_and_open_c = models.TextField(blank=True, null=True)
    other_than_full_and_o_desc = models.TextField(blank=True, null=True)
    recovered_materials_sustai = models.TextField(blank=True, null=True)
    recovered_materials_s_desc = models.TextField(blank=True, null=True)
    research = models.TextField(blank=True, null=True)
    research_description = models.TextField(blank=True, null=True)
    sea_transportation = models.TextField(blank=True, null=True)
    sea_transportation_desc = models.TextField(blank=True, null=True)
    labor_standards = models.TextField(blank=True, null=True)
    labor_standards_descrip = models.TextField(blank=True, null=True)
    small_business_competitive = models.NullBooleanField(blank=True)
    solicitation_identifier = models.TextField(blank=True, null=True)
    solicitation_procedures = models.TextField(blank=True, null=True)
    solicitation_procedur_desc = models.TextField(blank=True, null=True)
    fair_opportunity_limited_s = models.TextField(blank=True, null=True)
    fair_opportunity_limi_desc = models.TextField(blank=True, null=True)
    subcontracting_plan = models.TextField(blank=True, null=True)
    subcontracting_plan_desc = models.TextField(blank=True, null=True)
    program_system_or_equipmen = models.TextField(blank=True, null=True)
    program_system_or_equ_desc = models.TextField(blank=True, null=True)
    type_set_aside = models.TextField(blank=True, null=True, db_index=True)
    type_set_aside_description = models.TextField(blank=True, null=True)
    epa_designated_product = models.TextField(blank=True, null=True)
    epa_designated_produc_desc = models.TextField(blank=True, null=True)
    materials_supplies_article = models.TextField(blank=True, null=True)
    materials_supplies_descrip = models.TextField(blank=True, null=True)
    transaction_number = models.TextField(blank=True, null=True)
    sam_exception = models.TextField(blank=True, null=True)
    sam_exception_description = models.TextField(blank=True, null=True)
    city_local_government = models.NullBooleanField(blank=True)
    county_local_government = models.NullBooleanField(blank=True)
    inter_municipal_local_gove = models.NullBooleanField(blank=True)
    local_government_owned = models.NullBooleanField(blank=True)
    municipality_local_governm = models.NullBooleanField(blank=True)
    school_district_local_gove = models.NullBooleanField(blank=True)
    township_local_government = models.NullBooleanField(blank=True)
    us_state_government = models.NullBooleanField(blank=True)
    us_federal_government = models.NullBooleanField(blank=True)
    federal_agency = models.NullBooleanField(blank=True)
    federally_funded_research = models.NullBooleanField(blank=True)
    us_tribal_government = models.NullBooleanField(blank=True)
    foreign_government = models.NullBooleanField(blank=True)
    community_developed_corpor = models.NullBooleanField(blank=True)
    labor_surplus_area_firm = models.NullBooleanField(blank=True)
    corporate_entity_not_tax_e = models.NullBooleanField(blank=True)
    corporate_entity_tax_exemp = models.NullBooleanField(blank=True)
    partnership_or_limited_lia = models.NullBooleanField(blank=True)
    sole_proprietorship = models.NullBooleanField(blank=True)
    small_agricultural_coopera = models.NullBooleanField(blank=True)
    international_organization = models.NullBooleanField(blank=True)
    us_government_entity = models.NullBooleanField(blank=True)
    emerging_small_business = models.NullBooleanField(blank=True)
    c8a_program_participant = models.NullBooleanField(blank=True)
    sba_certified_8_a_joint_ve = models.NullBooleanField(blank=True)
    dot_certified_disadvantage = models.NullBooleanField(blank=True)
    self_certified_small_disad = models.NullBooleanField(blank=True)
    historically_underutilized = models.NullBooleanField(blank=True)
    small_disadvantaged_busine = models.NullBooleanField(blank=True)
    the_ability_one_program = models.NullBooleanField(blank=True)
    historically_black_college = models.NullBooleanField(blank=True)
    c1862_land_grant_college = models.NullBooleanField(blank=True)
    c1890_land_grant_college = models.NullBooleanField(blank=True)
    c1994_land_grant_college = models.NullBooleanField(blank=True)
    minority_institution = models.NullBooleanField(blank=True)
    private_university_or_coll = models.NullBooleanField(blank=True)
    school_of_forestry = models.NullBooleanField(blank=True)
    state_controlled_instituti = models.NullBooleanField(blank=True)
    tribal_college = models.NullBooleanField(blank=True)
    veterinary_college = models.NullBooleanField(blank=True)
    educational_institution = models.NullBooleanField(blank=True)
    alaskan_native_servicing_i = models.NullBooleanField(blank=True)
    community_development_corp = models.NullBooleanField(blank=True)
    native_hawaiian_servicing = models.NullBooleanField(blank=True)
    domestic_shelter = models.NullBooleanField(blank=True)
    manufacturer_of_goods = models.NullBooleanField(blank=True)
    hospital_flag = models.NullBooleanField(blank=True)
    veterinary_hospital = models.NullBooleanField(blank=True)
    hispanic_servicing_institu = models.NullBooleanField(blank=True)
    foundation = models.NullBooleanField(blank=True)
    woman_owned_business = models.NullBooleanField(blank=True)
    minority_owned_business = models.NullBooleanField(blank=True)
    women_owned_small_business = models.NullBooleanField(blank=True)
    economically_disadvantaged = models.NullBooleanField(blank=True)
    joint_venture_women_owned = models.NullBooleanField(blank=True)
    joint_venture_economically = models.NullBooleanField(blank=True)
    veteran_owned_business = models.NullBooleanField(blank=True)
    service_disabled_veteran_o = models.NullBooleanField(blank=True)
    contracts = models.NullBooleanField(blank=True)
    grants = models.NullBooleanField(blank=True)
    receives_contracts_and_gra = models.NullBooleanField(blank=True)
    airport_authority = models.NullBooleanField(blank=True)
    council_of_governments = models.NullBooleanField(blank=True)
    housing_authorities_public = models.NullBooleanField(blank=True)
    interstate_entity = models.NullBooleanField(blank=True)
    planning_commission = models.NullBooleanField(blank=True)
    port_authority = models.NullBooleanField(blank=True)
    transit_authority = models.NullBooleanField(blank=True)
    subchapter_s_corporation = models.NullBooleanField(blank=True)
    limited_liability_corporat = models.NullBooleanField(blank=True)
    foreign_owned_and_located = models.NullBooleanField(blank=True)
    american_indian_owned_busi = models.NullBooleanField(blank=True)
    alaskan_native_owned_corpo = models.NullBooleanField(blank=True)
    indian_tribe_federally_rec = models.NullBooleanField(blank=True)
    native_hawaiian_owned_busi = models.NullBooleanField(blank=True)
    tribally_owned_business = models.NullBooleanField(blank=True)
    asian_pacific_american_own = models.NullBooleanField(blank=True)
    black_american_owned_busin = models.NullBooleanField(blank=True)
    hispanic_american_owned_bu = models.NullBooleanField(blank=True)
    native_american_owned_busi = models.NullBooleanField(blank=True)
    subcontinent_asian_asian_i = models.NullBooleanField(blank=True)
    other_minority_owned_busin = models.NullBooleanField(blank=True)
    for_profit_organization = models.NullBooleanField(blank=True)
    nonprofit_organization = models.NullBooleanField(blank=True)
    other_not_for_profit_organ = models.NullBooleanField(blank=True)
    us_local_government = models.NullBooleanField(blank=True)
    referenced_idv_modificatio = models.TextField(blank=True, null=True)
    undefinitized_action = models.TextField(blank=True, null=True)
    undefinitized_action_desc = models.TextField(blank=True, null=True)
    domestic_or_foreign_entity = models.TextField(blank=True, null=True)
    domestic_or_foreign_e_desc = models.TextField(blank=True, null=True)
    annual_revenue = models.TextField(blank=True, null=True)
    division_name = models.TextField(blank=True, null=True)
    division_number_or_office = models.TextField(blank=True, null=True)
    number_of_employees = models.TextField(blank=True, null=True)
    vendor_alternate_name = models.TextField(blank=True, null=True)
    vendor_alternate_site_code = models.TextField(blank=True, null=True)
    vendor_enabled = models.TextField(blank=True, null=True)
    vendor_legal_org_name = models.TextField(blank=True, null=True)
    vendor_location_disabled_f = models.TextField(blank=True, null=True)
    vendor_site_code = models.TextField(blank=True, null=True)
    pulled_from = models.TextField(blank=True, null=True)
    last_modified = models.TextField(blank=True, null=True)
    initial_report_date = models.TextField(blank=True, null=True)
    cage_code = models.TextField(blank=True, null=True)
    inherently_government_func = models.TextField(blank=True, null=True)
    inherently_government_desc = models.TextField(blank=True, null=True)
    organizational_type = models.TextField(blank=True, null=True)
    referenced_idv_agency_name = models.TextField(blank=True, null=True)
    referenced_multi_or_single = models.TextField(blank=True, null=True)
    place_of_perform_country_n = models.TextField(blank=True, null=True)
    place_of_perform_state_nam = models.TextField(blank=True, null=True)
    unique_award_key = models.TextField(null=True, db_index=True)
    solicitation_date = models.DateField(null=True, blank=True)
    officer_1_name = models.TextField(null=True, blank=True)
    officer_1_amount = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    officer_2_name = models.TextField(null=True, blank=True)
    officer_2_amount = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    officer_3_name = models.TextField(null=True, blank=True)
    officer_3_amount = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    officer_4_name = models.TextField(null=True, blank=True)
    officer_4_amount = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    officer_5_name = models.TextField(null=True, blank=True)
    officer_5_amount = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)

    # Timestamp field auto generated by broker
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True, db_index=True)

    @classmethod
    def get_or_create_2(cls, transaction, **kwargs):
        try:
            if not transaction.newer_than(kwargs):
                for (k, v) in kwargs.items():
                    setattr(transaction.contract_data, k, v)
        except ObjectDoesNotExist:
            transaction.contract_data = cls(**kwargs)
        return transaction.contract_data

    class Meta:
        db_table = "transaction_fpds"
