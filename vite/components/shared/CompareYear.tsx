"use client";

import { useState } from "react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "../ui/dropdown-menu";
import { ArrowDown } from "lucide-react";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../ui/select";
import Link from "next/link";
import { Button } from "../ui/button";

function CompareYear() {
  const types = [
    "liquidity",
    "leverage",
    "profitability",
    "marketvalue",
    "assetsto ",
  ];
  const dates = [2022, 2023];
  const [year, setYear] = useState("");
  const [year2, setYear2] = useState("");
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
            Compare between years
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
            <Select value={year2} onValueChange={setYear2}>
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
              href={`/compare?years=${year},${year2}&type=${type}`}
            >
              <Button className="w-full mt-4">Go</Button>
            </Link>
          </div>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  );
}
export default CompareYear;
