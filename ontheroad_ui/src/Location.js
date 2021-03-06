import React from 'react';

import Button from 'react-bootstrap/Button';
import Table from 'react-bootstrap/Table';

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
        zoom: 9
    };

    constructor(props) {
        super(props);
        this.state = {
            address: '',
            latlng: {
                lat:"40.7643574",
                lng:"-73.92346189999999"
            },
            addresses: [],
            startingIndex: 0,
            name: '',
            placeID: null
        }
        this.handlePlacesChange = this.handlePlacesChange.bind(this)
        this.handlePlacesSelect = this.handlePlacesSelect.bind(this)

        this.onChange = (address) => {
          this.setState({ address, placeID: null, latlng: {lat:"0", lng:"0"}})
        }
        this.saveAddress = (address, placeID) => {
          this.setState({ address, placeID })
        }
        this.saveLocation = (latlng, address) =>  {
//          console.log(`latlng: ${latlng}, address: ${address}`)
//          this.setState({...this.state, latlng: latlng, address: address})
          this.setState({latlng: latlng, address: address})
        }
        this.handleChange = this.handleChange.bind(this);
        this.onAdd = this.onAdd.bind(this);
        this.onRemove = this.onRemove.bind(this);
        this.onSetStart = this.onSetStart.bind(this);
    }

    handleChange(e) {
        console.log(`Location::handleChange: ${e}`);
        this.props.onAddressesChange(e);
    }

    dump_addresses(addresses, special_message) {
      for(var i=0; i < addresses.length; i++) {
        console.log(`${special_message}: addresses[${i}][2]: ${addresses[i][2]}`);
      }
    }

    onAdd(e) {
      console.log(`Location.onAdd(): New address= ${this.state.address}`);

      var allAddresses = this.props.addresses;
      if(null === allAddresses) {
          allAddresses = [];
      }
      allAddresses.push([this.state.latlng.lat, this.state.latlng.lng, this.state.address]);
//      this.dump_addresses(allAddresses, "Location:POST");

      this.setState({
        addresses: allAddresses,
        address: ""
      });

      console.log(`this.state: ${this.state}`);
      window.localStorage.setItem("addresses", JSON.stringify(allAddresses));
      this.handleChange(allAddresses);
    }

    onRemove(index) {
      console.log(`Location.onRemove() index: = ${index}`);
      var allAddresses = this.props.addresses;
      allAddresses.splice(index, 1);
      this.setState({
        addresses: allAddresses
      });

      window.localStorage.setItem("addresses", JSON.stringify(allAddresses));
      this.handleChange(allAddresses);
    }

    onSetStart(index) {
      console.log(`Location.onSetStart() index: = ${index}`);
      var startingIndex = this.props.startingIndex;
      startingIndex = index;
      this.setState({
        startingIndex: startingIndex
      });
      this.props.onStartingIndexChange(index);
    }

    handlePlacesChange(address) {
      console.log(`PlacesAutoComplete.handlePlacesChange(): address=${address}`);
    }

    handlePlacesSelect(address, placeID) {
      console.log(`PlacesAutoComplete.handlePlacesSelect(): address=${address}, placeID=${placeID}`);
      this.saveAddress(address, placeID)
      geocodeByAddress(address)
        .then(results => getLatLng(results[0]) )
        .then(latlng => this.saveLocation(latlng, address) )
        .catch(error => console.error('Error', error));
    }

    render() {
        const addresses = this.props.addresses;
        const startingIndex = this.props.startingIndex;
        const {lat, lng} = this.state.latlng || {}
        const inputProps = {
            value: this.state.address,
            onChange: this.onChange
        }
        if(this.state.latlng && (this.state.latlng.lat !== "0" &&
                                 this.state.latlng.lng !== "0")) {
        }

        var destinations = addresses.map(function(name, index) {
                                  //console.log("Adding address: {name}:{index}");
                                  return  <tr key={index}>
                                            <td>{name[2].toString()}</td>
                                            <td><Button variant="secondary" onClick={() => {this.onRemove(index)}} size="sm">Remove</Button></td>
                                            <td><Button variant="secondary" onClick={() => {this.onSetStart(index)}} disabled={this.state.startingIndex == index}>Set as Start</Button></td>
                                          </tr>;
                                }.bind(this));
        return (
            <div className={"location.style"} >
                <div className="container no-padding">
                  <Table bordered hover variant="dark" style={{width: '100%'}}>
                    <tbody>

                    <tr>
                      <td >
                        <h3>Enter an Address:</h3>
                        <hr />
                          <PlacesAutocomplete
                            id="placesAutoComplete"
                            inputProps={inputProps}
                            onChange={this.handlePlacesChange}
                            onSelect={this.handlePlacesSelect}
                            styles={ defaultStyles }/>
                      </td>
                      <td>
                        <div>
                          <h3>Verify and click add:</h3>
                          <hr />
                          {
                          <div>
                            {
                            <MapWithRestaurant
                              loadingElement={<div style={{ height: `100%` }} />}
                              containerElement={<div style={{ height: `200px` }} />}
                              mapElement={<div style={{ height: `100%` }} />}
                              location={ this.state.latlng }
                              markers={ <Marker position={ {lat: parseFloat(lat), lng: parseFloat(lng)} } /> }
                            />
                            }
                            <Button variant="secondary" onClick={this.onAdd} size="sm">Add</Button>
                          </div>
                          }
                          {
                          /*
                            <ul>
                                {this.state.allAddresses.map(function(name, index){
                                                    return <li key={ index }>{name.toString()}</li>;
                                })
                                }
                            </ul>
                            */
                          }
                        </div>
                      </td>
                    </tr>
                    </tbody>
                  </Table>
                  <Table bordered hover variant="dark">
                    <thead>
                      <tr>
                        <th>You Entered the Following Addresses:</th>
                      </tr>
                    </thead>
                    <tbody>

                    <tr>
                      <td>
                          <Table bordered hover variant="dark">
                            <thead>
                              <tr>
                                <th>Address</th>
                                <th>Remove</th>
                                <th>Starting Point</th>
                              </tr>
                            </thead>
                            <tbody>
                                {destinations}
                            </tbody>
                          </Table>

                      </td>
                      </tr>
                    </tbody>
                    </Table>
                    <hr />
                </div>
            </div>
        );
    }
}

export default Location;