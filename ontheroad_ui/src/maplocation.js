import React, { Component } from 'react'
import {
  withScriptjs,
  withGoogleMap,
  GoogleMap,
  Marker,
} from "react-google-maps";

// lat: 40.7127753
// lng: -74.0059728
const MapWithRestaurant = withGoogleMap(props => {
  const {lat, lng} = props.location
  console.log("lat: " + lat)
  console.log("lng: " + lng)
  return(
  <GoogleMap
    defaultZoom={16}
    defaultCenter={ {lat: parseFloat(lat), lng: parseFloat(lng)} }
    center={ {lat: parseFloat(lat), lng: parseFloat(lng)} }
  >
    <Marker
      position={ {lat: parseFloat(lat), lng: parseFloat(lng)} }
    />
  </GoogleMap>
)
}
);

export default MapWithRestaurant