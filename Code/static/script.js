/**
 * 1. THE BASICS: What is a Callback?
 * A callback is simply a function passed as an argument to another function,
 * to be executed ("called back") after an operation finishes.
 */

// This function processes data and then hands the result off to whatever callback you give it
function processApplicantData(applicantName, callback) {
    console.log(`\n[1] Starting data processing for: ${applicantName}...`);
    
    // Simulate a data transformation task
    const cleanedData = {
        name: applicantName.toUpperCase(),
        status: "Cleaned",
        timestamp: new Date().toLocaleTimeString()
    };
    
    // Execute the callback function and pass the result to it
    callback(cleanedData);
}

// Defining our callback functions
function logToConsole(result) {
    console.log(`>>> CALLBACK RUNNING: Data successfully logged for ${result.name} at ${result.timestamp}.`);
}

function notifySystem(result) {
    console.log(`>>> CALLBACK RUNNING: Alerting internal server! Account ${result.name} is ready.`);
}

// Running the functions with different callbacks
processApplicantData("Alice Smith", logToConsole);
processApplicantData("Bob Jones", notifySystem);


/**
 * 2. REAL-WORLD USE CASE: Handling Errors in Callbacks
 * In Node.js and real JavaScript development, callbacks usually follow the "Error-First" pattern.
 * The first argument is reserved for an error (if something broke), and the second is the data.
 */

function verifyCreditScore(score, callback) {
    console.log(`\n[2] Evaluating credit score: ${score}...`);
    
    // Simulate a brief operational delay
    setTimeout(() => {
        if (score < 300 || score > 850) {
            // If the score is invalid, pass an error object to the callback
            callback(new Error("Invalid Credit Score range. Must be between 300 and 850."), null);
        } else {
            // If valid, pass null for the error, and return the evaluation data
            const decision = score >= 700 ? "Approved" : "Referred to Manual Review";
            callback(null, { score: score, decision: decision });
        }
    }, 1000); // 1-second delay
}

// Executing the Error-First callback
verifyCreditScore(750, (error, data) => {
    if (error) {
        console.error("❌ Process Failed:", error.message);
        return;
    }
    console.log(`✅ Process Succeeded! Decision: ${data.decision} (Score: ${data.score})`);
});

// Executing with an invalid input to trigger the error handling path
verifyCreditScore(999, (error, data) => {
    if (error) {
        console.error("❌ Process Failed:", error.message);
        return;
    }
    console.log(`✅ Process Succeeded! Decision: ${data.decision}`);
});


/**
 * 3. THE PROBLEM: "Callback Hell" (Pyramid of Doom)
 * When you must perform multiple sequential asynchronous actions, nesting callbacks 
 * inside callbacks makes code unreadable. This is why modern JS uses Promises/Async-Await.
 */

function loadCSV(filename, callback) {
    setTimeout(() => { console.log(`\nFile '${filename}' loaded.`); callback(null, filename); }, 500);
}

function dropDuplicates(file, callback) {
    setTimeout(() => { console.log("Duplicates dropped."); callback(null); }, 500);
}

function handleMissingValues(callback) {
    setTimeout(() => { console.log("Missing values imputed."); callback(null); }, 500);
}

// The Nested "Pyramid of Doom"
loadCSV("application_record.csv", (err, file) => {
    if (!err) {
        dropDuplicates(file, (err) => {
            if (!err) {
                handleMissingValues((err) => {
                    if (!err) {
                        console.log("🎉 SUCCESS: Pipeline finished using nested callbacks!");
                    }
                });
            }
        });
    }
});