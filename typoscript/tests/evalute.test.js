import * as peggy from "peggy";
import * as jspeg from "../src/jspeg";
import * as evaluter from "../src/evaluter";
import * as env from "../src/env";

describe("Evaluter Tests", () => {
  let parser;
  let evaluer;
  let environment;
  let output = "";

  beforeAll(() => {
    parser = peggy.generate(jspeg.peg_rule);
    evaluer = new evaluter.Evaluter();
  });

  beforeEach(() => {
    output = "";
    environment = new env.Env();
  });

  test("evaluate print(1)", () => {
    environment.native_functions.print = (x) => {
      output += x + "\n";
    };
    environment.native_functions.prompt = null;

    const ast = parser.parse("print(1)");
    evaluer.evalute(environment, ast);
    expect(output.trim()).toEqual("1");
  });

  test("evaluate for", () => {
    environment.native_functions.print = (x) => {
      output += x + "\n";
    };
    environment.native_functions.prompt = null;

    const ast = parser.parse(`
    var x=0;
    for(var i=0;i<10;i++){
        x++
    }
    print(x)`);
    evaluer.evalute(environment, ast);
    expect(output.trim()).toEqual("10");
  });
});
