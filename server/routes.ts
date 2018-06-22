import * as express from 'express';
import GenerateCtrl from './controllers/generate';
import ContactCtrl from './controllers/contact';
import InferrerCtrl from './controllers/inferrer';

export default function setRoutes(app) {

  const router = express.Router();

  const generateCtrl = new GenerateCtrl();
  const contactCtrl = new ContactCtrl();
  const inferrerCtrl = new InferrerCtrl();

  router.route('/generate').post(generateCtrl.generateRegex);
  router.route('/inferrer').post(inferrerCtrl.inferGrammar);
  router.route('/contact').post(contactCtrl.sendEmail);

  /* apply the routes to our application with the prefix /api */
  app.use('/api', router);

}
