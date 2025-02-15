from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class YieldDiscPostRequestBody(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def basis(self,) -> Optional[json.Json]:
        """
        Gets the basis property value. The basis property
        Returns: Optional[json.Json]
        """
        return self._basis
    
    @basis.setter
    def basis(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the basis property value. The basis property
        Args:
            value: Value to set for the basis property.
        """
        self._basis = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new yieldDiscPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The basis property
        self._basis: Optional[json.Json] = None
        # The maturity property
        self._maturity: Optional[json.Json] = None
        # The pr property
        self._pr: Optional[json.Json] = None
        # The redemption property
        self._redemption: Optional[json.Json] = None
        # The settlement property
        self._settlement: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> YieldDiscPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: YieldDiscPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return YieldDiscPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "basis": lambda n : setattr(self, 'basis', n.get_object_value(json.Json)),
            "maturity": lambda n : setattr(self, 'maturity', n.get_object_value(json.Json)),
            "pr": lambda n : setattr(self, 'pr', n.get_object_value(json.Json)),
            "redemption": lambda n : setattr(self, 'redemption', n.get_object_value(json.Json)),
            "settlement": lambda n : setattr(self, 'settlement', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def maturity(self,) -> Optional[json.Json]:
        """
        Gets the maturity property value. The maturity property
        Returns: Optional[json.Json]
        """
        return self._maturity
    
    @maturity.setter
    def maturity(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the maturity property value. The maturity property
        Args:
            value: Value to set for the maturity property.
        """
        self._maturity = value
    
    @property
    def pr(self,) -> Optional[json.Json]:
        """
        Gets the pr property value. The pr property
        Returns: Optional[json.Json]
        """
        return self._pr
    
    @pr.setter
    def pr(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the pr property value. The pr property
        Args:
            value: Value to set for the pr property.
        """
        self._pr = value
    
    @property
    def redemption(self,) -> Optional[json.Json]:
        """
        Gets the redemption property value. The redemption property
        Returns: Optional[json.Json]
        """
        return self._redemption
    
    @redemption.setter
    def redemption(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the redemption property value. The redemption property
        Args:
            value: Value to set for the redemption property.
        """
        self._redemption = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("basis", self.basis)
        writer.write_object_value("maturity", self.maturity)
        writer.write_object_value("pr", self.pr)
        writer.write_object_value("redemption", self.redemption)
        writer.write_object_value("settlement", self.settlement)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def settlement(self,) -> Optional[json.Json]:
        """
        Gets the settlement property value. The settlement property
        Returns: Optional[json.Json]
        """
        return self._settlement
    
    @settlement.setter
    def settlement(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the settlement property value. The settlement property
        Args:
            value: Value to set for the settlement property.
        """
        self._settlement = value
    

