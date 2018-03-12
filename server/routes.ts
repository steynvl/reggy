import * as express from 'express';
import GenerateCtrl from './controllers/generate';

export default function setRoutes(app) {

  const router = express.Router();

  const generateCtrl = new GenerateCtrl();

  router.route('/generate').post(generateCtrl.generate);

  // Apply the routes to our application with the prefix /api
  app.use('/api', router);

}
