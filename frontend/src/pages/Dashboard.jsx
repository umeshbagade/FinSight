import { useEffect, useState } from "react";

import { getCashflowForecast } from "../api/client";


function Dashboard() {
  const [cashflow, setCashflow] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadCashflow() {
      try {
        const data = await getCashflowForecast();
        setCashflow(data);
      } catch (err) {
        setError(err.message);
      }
    }

    loadCashflow();
  }, []);

  if (error) {
    return <p>{error}</p>;
  }

  if (!cashflow) {
    return <p>Loading...</p>;
  }

  return (
    <main>
      <h1>FinSight</h1>

      <p>Your AI-powered financial advisor for SMEs.</p>

      <section>
        <h2>Business Overview</h2>

        <p>Current Balance: €{cashflow.current_balance}</p>

        <p>
          Projected Balance: €{cashflow.forecast_balance}
        </p>

        <p>Cash Flow Risk: {cashflow.risk_level}</p>

        <p>{cashflow.insight}</p>
      </section>
    </main>
  );
}

export default Dashboard;