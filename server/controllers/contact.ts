import BaseCtrl from './base';

export default class ContactCtrl extends BaseCtrl {

  model = null;

  sendEmail = (req, res) => {
    const info = req.body.params;

    console.log('--- contact ---');
    console.log(info);
    console.log('--- contact ---');

    res.send(JSON.stringify('Hello'));
  }

}
