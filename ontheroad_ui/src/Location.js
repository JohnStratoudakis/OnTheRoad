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
        zoom: 7
    };

    constructor(props) {
        super(props);
        this.state = {
            address: '',
            latlng: {
                lat:"0",
                lng:"0"
            },
            allAddresses: [],
            name: '',
            placeID: null,
            guest: null
        }
        this.getPlace = this.getPlace.bind(this)
        this.onChange = (address) => this.setState({ address, placeID: null, latlng: {lat:"0", lng:"0"}, guest: null })
        this.saveAddress = (address, placeID) => this.setState({ address, placeID })
        this.saveLocation = (latlng, address) =>  {
          console.log(`latlng: ${latlng}, address: ${address}`)
          this.setState({...this.state, latlng: latlng, address: address})
        }
        this.onAdd = this.onAdd.bind(this);
//        {allAddresses} = this.state
    }

    dump_addresses(addresses) {
      console.log(`addresses.length: ${addresses.length}`);
      for(var i=0; i < addresses.length; i++) {
        var element = addresses[i];
        console.log(`element.length: ${element.length}`)
        for(var j=0; j < element.length; j++) {
          console.log(`addresses[${i}][${j}]: ${addresses[i][j]}`);
        }
      }
    }

    onAdd() {
      console.log("onAdd called.");
      console.log(`lat: ${this.state.latlng.lat}, lng: ${this.state.latlng.lng}`);
      console.log(`New address: ${this.state.address}`);

      var allAddresses = this.state.allAddresses;
      this.dump_addresses(allAddresses);
      allAddresses.push(new Array(this.state.latlng.lat, this.state.latlng.lng, this.state.address))
      this.dump_addresses(allAddresses);

      this.setState({
        allAddresses: allAddresses
      });
//      console.log(`this.state.allAddresses.length: ${this.state.allAddresses.length}`);
//      for(var i=0; i < this.state.allAddresses.length; i++) {
//        console.log(`this.state.allAddresses[${i}]: ${this.state.allAddresses[i]}`);
//      }
    }

    getPlace(address, placeID) {
        this.saveAddress(address, placeID)
        geocodeByAddress(address)
            .then(results => getLatLng(results[0]) )
            .then(latlng => this.saveLocation(latlng, address) )
            .catch(error => console.error('Error', error))
    }

    render() {
        const {lat, lng} = this.state.latlng || {}
        const inputProps = {
            value: this.state.address,
            onChange: this.onChange
        }
        if(this.state.latlng && (this.state.latlng.lat !== "0" &&
                                 this.state.latlng.lng !== "0")) {
          console.log(`lat: ${this.state.latlng.lat}`);
          console.log(`lng: ${this.state.latlng.lng}`);
        }

        return (
            <div className={"location.style"} >
                <div className="container no-padding border">
                  <Table bordered hover variant="dark" style={{width: '100%'}}>
                    <tbody>

                    <tr>
                      <td >
                        <h1>Enter Address</h1>
                        <hr />
                          <PlacesAutocomplete inputProps={inputProps} onSelect={this.getPlace} styles={ defaultStyles }/>
                      </td>
                      <td>
                        <div>
                          <h3>All Addresses:</h3>
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
                        <th>Selected Locations</th>
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
                              </tr>
                            </thead>
                            <tbody>
                                {
                                this.state.allAddresses.map(function(name, index){
                                  return  <tr>
                                            <td>{name[2].toString()}</td>
                                            <td>{index}</td>
                                          </tr>;
                                })
                                }
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