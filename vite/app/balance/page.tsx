"use client";
import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

interface Balance {
  formula: string;
  numbers: string;
  type: string;
  value: number;
}

function Balance() {
  const [years, setYears] = useState<Balance[]>([]);
  const params = useSearchParams();
  const year = params.get("years");
  const type = params.get("type");

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(
        `http://127.0.0.1:8000/api/v1/balance?years=${year}&type=${type}&company=sample_company`
      );
      const data = await response.json();

      if (Array.isArray(data)) {
        setYears(data);
      } else if (data && data.hasOwnProperty(year)) {
        const balances = data[year!];
        setYears(balances);
      } else {
        console.error("Invalid response data:", data);
      }
    };

    fetchData();
  }, [year, type]);

  console.log(years);
  return (
    <>
      <h2 className="text-center font-bold text-2xl my-5">{year}</h2>
      <div className="overflow-x-auto rounded-lg border border-gray-200">
        <table className="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead className="ltr:text-left rtl:text-right">
            <tr>
              <th className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Ratio
              </th>
              <th className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Formula
              </th>
              <th className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Numbers
              </th>
              <th className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Value
              </th>
            </tr>
          </thead>

          <tbody className="divide-y divide-gray-200 text-center">
            {years?.map((year) => (
              <tr key={year?.type}>
                <td className="whitespace-nowrap px-4 py-2 font-medium text-gray-900 cursor-pointer">
                  {year?.type}
                </td>
                <td className="whitespace-nowrap px-4 py-2 text-gray-700">
                  {year?.formula}
                </td>
                <td className="whitespace-wrap max-w-[70px] px-4 py-2 text-gray-700">
                  {year?.numbers}
                </td>
                <td className="whitespace-nowrap px-4 py-2 text-gray-700">
                  {year?.value}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default Balance;
