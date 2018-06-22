import { spawnChildProcess } from './generate';

export default class InferrerCtrl {

  inferGrammar = (req, res) => {
    const samples = req.body.params;

    const py = spawnChildProcess(samples);
    let output = '';

    py.stdout.on('data', (data) => {
      output += data.toString();
    });

    py.on('close', (code) => {
      res.setHeader('Content-Type', 'application/json');

      let deserialized;
      if (code === 0) {
        deserialized = JSON.parse(output);
      }

      const serverResponse: ServerResponse = {
        regex        : deserialized.regex,
        code         : code
      };

      res.send(JSON.stringify(serverResponse));
    });

  }

}

interface ServerResponse {
  code: number;
  regex: string;
}
