from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class ExactPostRequestBody(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new exactPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The text1 property
        self._text1: Optional[json.Json] = None
        # The text2 property
        self._text2: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExactPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "text1": lambda n : setattr(self, 'text1', n.get_object_value(json.Json)),
            "text2": lambda n : setattr(self, 'text2', n.get_object_value(json.Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("text1", self.text1)
        writer.write_object_value("text2", self.text2)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def text1(self,) -> Optional[json.Json]:
        """
        Gets the text1 property value. The text1 property
        Returns: Optional[json.Json]
        """
        return self._text1
    
    @text1.setter
    def text1(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the text1 property value. The text1 property
        Args:
            value: Value to set for the text1 property.
        """
        self._text1 = value
    
    @property
    def text2(self,) -> Optional[json.Json]:
        """
        Gets the text2 property value. The text2 property
        Returns: Optional[json.Json]
        """
        return self._text2
    
    @text2.setter
    def text2(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the text2 property value. The text2 property
        Args:
            value: Value to set for the text2 property.
        """
        self._text2 = value
    

