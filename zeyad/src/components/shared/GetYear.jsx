import { Link } from "react-router-dom";
import { Button } from "../ui/button";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../ui/select";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "../ui/dropdown-menu";
import { ArrowDown } from "lucide-react";
import { useState } from "react";
import CompareYears from "./CompareYears";
function GetYear() {
  const types = [
    "Liquidity",
    "Leveraging",
    "Profitability",
    "Market Value",
    "AssetsTo ",
  ];
  const years = [2022, 2021, 2020, 2019];
  const [year, setYear] = useState("");
  const [type, setType] = useState("");
  return (
    <div className="flex items-center justify-center gap-4">
      <DropdownMenu>
        <DropdownMenuTrigger asChild>
          <h2
            className="hidden md:flex gap-2 items-center
    border rounded-full p-2 px-10 bg-slate-200 cursor-pointer
"
          >
            Ratio of one year
            <ArrowDown className="h-5 w-5 animate-bounce" />
          </h2>
        </DropdownMenuTrigger>
        <DropdownMenuContent className="w-56 gap-4">
          <DropdownMenuLabel>Choose year</DropdownMenuLabel>
          <DropdownMenuSeparator />
          <div className="flex flex-col items-center justify-center gap-4">
            <Select value={year} onValueChange={setYear}>
              <SelectTrigger className="w-full">
                <SelectValue placeholder="Select year" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  {years.map((year) => (
                    <SelectItem key={year} value={year}>
                      {year}
                    </SelectItem>
                  ))}
                </SelectGroup>
              </SelectContent>
            </Select>
            <Select value={type} onValueChange={setType}>
              <SelectTrigger className="w-full">
                <SelectValue placeholder="Select type" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  {types.map((type) => (
                    <SelectItem key={type} value={type}>
                      {type}
                    </SelectItem>
                  ))}
                </SelectGroup>
              </SelectContent>
            </Select>
            <Link
              className="w-full gap-0"
              to={`/balance?years=${year}&type=${type}`}
            >
              <Button className="w-full mt-4">Go</Button>
            </Link>
          </div>
        </DropdownMenuContent>
      </DropdownMenu>
      <CompareYears />
    </div>
  );
}

export default GetYear;
