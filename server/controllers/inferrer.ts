import * as path from 'path';
import * as child_process from 'child_process';

export default class InferrerCtrl {

  inferGrammar = (req, res) => {
    const samples = req.body.params;
    console.log('---------');
    console.log(samples);
    console.log('---------');

    const py = spawnChildProcess(samples);
    let output = '';

    py.stdout.on('data', (data) => {
      output += data.toString();
    });

    py.on('close', (code) => {
      res.setHeader('Content-Type', 'application/json');
      const samplesObj = JSON.parse(samples);

      let deserialized;
      if (code === 0) {
        deserialized = JSON.parse(output);

        if (samplesObj.algorithm === 'interactive lstar') {
          deserialized.code = 0;
          res.send(JSON.stringify(deserialized));
        } else {
          const serverResponse: ServerResponse = {
            regex        : deserialized.regex,
            dot          : deserialized.dot,
            code         : code
          };

          res.send(JSON.stringify(serverResponse));
        }
      } else {
        res.send(JSON.stringify({code: 1}));
      }

    });

  }

}

function spawnChildProcess(info) {
  const pathToMain = path.join(__dirname, '..', '..', '..', 'server', 'reggy', 'reggy', 'inference',  'main.py');
  return child_process.spawn('python3', [pathToMain].concat(info));
}

interface ServerResponse {
  code: number;
  regex: string;
  dot: string;
}
