"use client";

import { Loader2, Ratio } from "lucide-react";
import { useRouter, useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

interface Balance {}

function Compare() {
  // const [date1, setDate1] = useState([]);
  // const [date2, setDate2] = useState([]);
  // const [ratios, setRatios] = useState([]);
  // const router = useRouter();
  // const params = useSearchParams();
  // const yearParam = params.get("years");
  // const year1 = yearParam ? yearParam.split(",")[0] : null;
  // const year2 = yearParam ? yearParam.split(",")[1] : null;
  // const type = params.get("type");

  // if (!year1 || !year2) {
  //   router.push(`/balance?years=${!year1 ? year2 : year1}&type=${type}`);
  //   return (
  //     <div className="flex items-center justify-center text-center">
  //       <Loader2 className="h-16 w-16 animate-spin" />
  //     </div>
  //   );
  // }

  // // eslint-disable-next-line react-hooks/rules-of-hooks
  // useEffect(() => {
  //   const fetchData = async () => {
  //     const response = await fetch(
  //       `http://127.0.0.1:8000/api/v1/balance?years=${year1},${year2}&type=${type}&company=sample_company`
  //     );
  //     const data = await response.json();

  //     setDate1(data[year1]);
  //     setDate2(data[year2]);
  //     setRatios(data["ratios"]);
  //   };
  //   fetchData();
  // }, [type, year1, year2]);

  // console.log(date1, date2, ratios);

  const ratios = {
    ratios: ["Current Ratio", "Quick Ratio", "Cash Ratio"],
    date1: [78.35, 78.0, 0.1],
    date2: [8.93, 7.09, 1.0],
  };

  return (
    <div className="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8 mt-6">
      <div className="flex items-center justify-center text-center gap-10 mb-5">
        <h2 className="text-3xl font-bold mr-10 underline"></h2>
        <h2 className="text-3xl font-bold underline"></h2>
      </div>
      <div className="overflow-x-auto rounded-lg border border-gray-200">
        <table className="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
          <thead className="ltr:text-left rtl:text-right">
            <tr>
              <th className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Ratios
              </th>
              <th className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Date 1
              </th>
              <th className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                Date 2
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200 text-center">
            {/* {ratios.map((ratio, index) => (
              <tr key={index}>
                <td className="whitespace-nowrap px-4 py-2 font-medium text-gray-900">
                  {ratio}
                </td>
                <td className="whitespace-nowrap px-4 py-2 text-gray-700">
                  {date1[index]}
                </td>
                <td className="whitespace-nowrap px-4 py-2 text-gray-700">
                  {date2[index]}
                </td>
              </tr>
            ))} */}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Compare;
