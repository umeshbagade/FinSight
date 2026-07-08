export async function getCashflowForecast() {
  const response = await fetch("/api/cashflow/forecast");

  if (!response.ok) {
    const body = await response.text();

    throw new Error(
      `Failed to fetch cashflow forecast: ${response.status} ${body}`
    );
  }

  return response.json();
}