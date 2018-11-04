/**
 * A container class for the markers on the 
 * sample-based generation component. 
 */
export class Container {

  constructor(public id: number,
              public markers: Array<Marker>) { }

}

interface Marker {
  id: number;
  colour: string;
}
