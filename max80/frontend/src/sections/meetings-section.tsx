import CardLink2 from "../components/card-link2";
import { CardLink2_cids2 } from "../_cids";
import { CardLink2_styles2 } from "../_styles";
import { cardLink2Data2 as cardLink2Data2Content } from "../content";
/** Meetings section. */
export default function MeetingsSection({ cardLink2Data2 = cardLink2Data2Content } = {}) {
  return (
    <div className="flex flex-col gap-4" data-cid="n233">
      <div className="flex flex-col gap-1" data-cid="n234">
        <h2 className="block text-color-001 text-xl font-semibold leading-7" data-cid="n235" data-component="heading">
          Meetings
        </h2>
      </div>
      <div className="grid gap-4 grid-rows-[72px] grid-cols-3 max-md:grid-rows-[72px_72px_72px] max-md:grid-cols-1 md:max-lg:grid-rows-[72px_72px] md:max-lg:grid-cols-2" data-cid="n236">
        {cardLink2Data2.map((d, i) => <CardLink2 key={i} d={d} cids={CardLink2_cids2[i]} styles={CardLink2_styles2[i]} />)}
      </div>
    </div>
  );
}
