import * as nodemailer from 'nodemailer';

export default class ContactCtrl {

  sendEmail = (req, res) => {
    const email = process.env.EMAIL;
    const pass  = process.env.PASSWORD;

    if (!email || !pass) {
      res.send(JSON.stringify({ msg: 'fail' }));
    }

    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: email,
        pass: pass
      }
    });

    const reqBody = JSON.parse(req.body.params);
    const mailOptions = {
      from: email,
      to: email,
      subject: `Reggy Contact Us: ${reqBody.category}`,
      text: `${reqBody.message}\n\nname: ${reqBody.name}\nemail: ${reqBody.email}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        res.send(JSON.stringify({ msg: 'fail' }));
      } else {
        res.send(JSON.stringify({ msg: 'success' }));
      }
    });
  };

}
