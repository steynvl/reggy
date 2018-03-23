import * as express from 'express';
import GenerateSamplesCtrl from './controllers/generate-samples';
import GenerateCommonCtrl from './controllers/generate-common';
import GenerateInductionCtrl from './controllers/generate-induction';

export default function setRoutes(app) {

  const router = express.Router();

  const generateSamplesCtrl = new GenerateSamplesCtrl();
  const generateCommonCtrl = new GenerateCommonCtrl();
  const generateInductionCtrl = new GenerateInductionCtrl();

  router.route('/generate/samples').post(generateSamplesCtrl.generate);
  router.route('/generate/common').post(generateCommonCtrl.generate);
  router.route('/generate/induction').post(generateInductionCtrl.generate);

  // Apply the routes to our application with the prefix /api
  app.use('/api', router);

}
