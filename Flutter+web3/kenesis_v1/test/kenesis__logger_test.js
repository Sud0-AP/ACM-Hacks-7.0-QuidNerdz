const Kenesis_Logger_test = artifacts.require("Kenesis_Logger_test");

/*
 * uncomment accounts to access the test accounts made available by the
 * Ethereum client
 * See docs: https://www.trufflesuite.com/docs/truffle/testing/writing-tests-in-javascript
 */
contract("Kenesis_Logger_test", function (/* accounts */) {
  it("should assert true", async function () {
    await Kenesis_Logger_test.deployed();
    return assert.isTrue(true);
  });
});
