import BaseCtrl from './base';

export default class GenerateCtrl extends BaseCtrl {

  model = null;

  generate = (req, res) => {
    const samples = Object.values(req.query);

    console.log(samples);

    res.setHeader('Content-Type', 'application/json');
    res.send(samples);
  }



}

