import * as express from 'express';
import GenerateCtrl from './controllers/generate';
import ContactCtrl from './controllers/contact';

export default function setRoutes(app) {

  const router = express.Router();

  const generateCtrl = new GenerateCtrl();
  const contactCtrl = new ContactCtrl();

  router.route('/generate').post(generateCtrl.generate);
  router.route('/contact').post(contactCtrl.sendEmail);

  // Apply the routes to our application with the prefix /api
  app.use('/api', router);

}
