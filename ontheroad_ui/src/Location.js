import React from 'react';

import Button from 'react-bootstrap/Button';
//import ButtonGroup from 'react-bootstrap/Button';
import PlacesAutocomplete from 'react-places-autocomplete';
import {
    geocodeByAddress,
//    geocodeByPlaceId,
    getLatLng
} from 'react-places-autocomplete';

import {
//  withScriptjs,
//  withGoogleMap,
//  GoogleMap,
  Marker } from "react-google-maps";
import MapWithRestaurant from './maplocation.js';

const defaultStyles = {
  root: {
    position: 'relative',
    paddingBottom: '0px',
  },
  input: {
    display: 'inline-block',
    width: '100%',
    padding: '10px',
  },
  autocompleteContainer: {
    position: 'absolute',
    top: '100%',
    backgroundColor: 'white',
    border: '1px solid #555555',
    width: '100%',
  },
  autocompleteItem: {
    backgroundColor: '#ffffff',
    padding: '10px',
    color: '#555555',
    cursor: 'pointer',
  },
  autocompleteItemActive: {
    backgroundColor: '#fafafa'
  },
  googleLogoContainer: {
    textAlign: 'right',
    padding: '1px',
    backgroundColor: '#fafafa'
  },
  googleLogoImage: {
    width: 150
  }
}

class Location extends React.Component {
    static defaultProps = {
        center: {lat: "48.8566", lng: "2.3522"},
        zoom: 7
    };

    constructor(props) {
        super(props);
        this.state = { address: '', latlng: {lat:"0", lng:"0"}, name: '', placeID: null, guest: null }
        this.getPlace = this.getPlace.bind(this)
        this.onChange = (address) => this.setState({ address, placeID: null, latlng: {lat:"0", lng:"0"}, guest: null })
        this.saveAddress = (address, placeID) => this.setState({ address, placeID })
        this.saveLocation = (latlng) => this.setState({...this.state, latlng: latlng})
    }

    getPlace(address, placeID) {
        this.saveAddress(address, placeID)
        geocodeByAddress(address)
            .then(results => getLatLng(results[0]) )
            .then(latlng => this.saveLocation(latlng) )
            .catch(error => console.error('Error', error))
    }

    render() {
        const {lat, lng} = this.state.latlng || {}
        const inputProps = {
            value: this.state.address,
            onChange: this.onChange
        }
        if(this.state.latlng) {
          console.log(`lat: ${this.state.latlng.lat}`);
          console.log(`lng: ${this.state.latlng.lng}`);
        }
        return (
            <div className={"location.style"} >
                <div className="container no-padding">
                    <h1>Location</h1>
                    <hr />
                    <PlacesAutocomplete inputProps={inputProps} onSelect={this.getPlace} styles={ defaultStyles }/>
                    <hr />
                    {
                    this.state.latlng && this.state.latlng.lat !== "0"
                                      && this.state.latlng.lng !== "0" &&
                    <div>
                      <h3>Lat: {this.state.latlng.lat}</h3>
                      <h3>Lng: {this.state.latlng.lng}</h3>
                      {
                      <MapWithRestaurant
                        loadingElement={<div style={{ height: `100%` }} />}
                        containerElement={<div style={{ height: `200px` }} />}
                        mapElement={<div style={{ height: `100%` }} />}
                        location={ this.state.latlng }
                        markers={ <Marker position={ {lat: parseFloat(lat), lng: parseFloat(lng)} } /> }
                      />
                      }
                      <Button variant="secondary">Add</Button>
                    </div>
                    }
                </div>
            </div>
        );
    }
}

export default Location;