export class Container {

  constructor(public id: number,
              public markers: Array<Marker>) { }

}

interface Marker {
  id: number;
  colour: string;
}
