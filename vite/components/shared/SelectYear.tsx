"use client";
import { ArrowDown } from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "../ui/dropdown-menu";
import { Button } from "../ui/button";
import Link from "next/link";
import { useState } from "react";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../ui/select";
const SelectYear = () => {
  const types = [
    "liquidity",
    "leverage",
    "profitability",
    "marketvalue",
    "assetsto ",
  ];
  const dates = [2022, 2023];
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
                  {dates?.map((date) => (
                    <SelectItem key={date} value={date}>
                      {date}
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
              href={`/balance?years=${year}&type=${type}`}
              //   to={`/balance?years=${year}&type=${type}`}
            >
              <Button className="w-full mt-4">Go</Button>
            </Link>
          </div>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  );
};

export default SelectYear;
