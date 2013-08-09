# -*- coding: utf-8 -*-
"""
    __init__

    Initialize Module

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from magento_ import (
    Instance, InstanceWebsite, WebsiteStore, WebsiteStoreView,
    TestConnectionStart, TestConnection, ImportWebsitesStart, ImportWebsites,
    ExportInventoryStart, ExportInventory, StorePriceTier,
    ExportTierPricesStart, ExportTierPrices, ExportTierPricesStatus,
)
from party import Party, MagentoWebsiteParty, Address
from product import (
    Category, MagentoInstanceCategory, Template, MagentoWebsiteTemplate,
    ImportCatalogStart, ImportCatalog, UpdateCatalogStart, UpdateCatalog,
    ProductPriceTier, ExportCatalogStart, ExportCatalog
)
from country import Country, Subdivision
from currency import Currency
from carrier import MagentoInstanceCarrier
from sale import MagentoOrderState, Sale, ImportOrdersStart, ImportOrders


def register():
    """
    Register classes
    """
    Pool.register(
        Instance,
        InstanceWebsite,
        WebsiteStore,
        StorePriceTier,
        WebsiteStoreView,
        MagentoInstanceCarrier,
        TestConnectionStart,
        ImportWebsitesStart,
        ExportInventoryStart,
        ExportTierPricesStart,
        ExportTierPricesStatus,
        Country,
        Subdivision,
        Party,
        MagentoWebsiteParty,
        Category,
        MagentoInstanceCategory,
        Template,
        MagentoWebsiteTemplate,
        ProductPriceTier,
        ImportCatalogStart,
        ExportCatalogStart,
        MagentoOrderState,
        Address,
        UpdateCatalogStart,
        Currency,
        Sale,
        ImportOrdersStart,
        module='magento', type_='model'
    )
    Pool.register(
        TestConnection,
        ImportWebsites,
        ExportInventory,
        ExportTierPrices,
        ImportCatalog,
        UpdateCatalog,
        ExportCatalog,
        ImportOrders,
        module='magento', type_='wizard'
    )