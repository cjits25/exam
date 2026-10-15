const { Builder, By, until } = require('selenium-webdriver');

(async function loginTest() {
  let driver = await new Builder().forBrowser('chrome').build();

  try {
    // Open your page (use http://localhost/... if using XAMPP)
    await driver.get('http://localhost/exp11/login.html');

    // Wait a bit for the page to load
    await driver.sleep(1000);

    // Enter username and password
    await driver.findElement(By.id('username')).sendKeys('suresh');
    await driver.findElement(By.id('password')).sendKeys('12345');

    // Click login button
    await driver.findElement(By.id('loginButton')).click();

    // Wait until message appears
    let message = await driver.wait(until.elementLocated(By.id('message')), 2000);
    let text = await message.getText();

    console.log("Message displayed:", text);
    if (text === "Login successful!") {
      console.log("✅ Test Passed!");
    } else {
      console.log("❌ Test Failed!");
    }

  } catch (err) {
    console.error("Test Error:", err);
  } finally {
    await driver.quit();
  }
})();
